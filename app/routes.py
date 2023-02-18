# -*- coding: utf-8 -*-


from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, UsermoveForm
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user
from flask_login import login_required
from flask import request, session
from werkzeug.urls import url_parse


@login_required
@app.route('/')
@app.route('/home')
def home():
    if current_user.is_authenticated:
        return render_template('home.html', title='Home')
    else:
        return render_template('login.html', title='login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        session['authorized'] = user.id
        session['role'] = user.role
        session['name'] = user.name
        session['checkpoint'] = user.checkpoint_current
        session['surname'] = user.surname
        print(user.name)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page), user
    return render_template('login.html', title='Sign In', form=form)


@login_required
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/move_user', methods=['GET', 'POST'])
def move_user():
    if session['role'] == 'HR':
        form = UsermoveForm()
        if form.validate_on_submit():
            chosen_user = User.query.filter_by(id=form.user_id.data).first()
            chosen_user.checkpoint = form.checkpoint_number.data
        return render_template('moving_user.html', title='Move User', form=form)
