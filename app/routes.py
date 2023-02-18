# -*- coding: utf-8 -*-
import requests

from app import app
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
@app.route('/index')
def index():
    user = {'username': 'Эльдар Рязанов'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
                # or not user.check_password(form.password.data)
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        session['authorized'] = user.id
        session['role'] = user.role
        print(user.role)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@login_required
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/move_user', methods=['GET', 'POST'])
def move_user():
    if session['role'] == 'HR':
        form = UsermoveForm()
        if form.validate_on_submit():
            chosen_user = User.query.filter_by(id=form.user_id.data).first()
            chosen_user.checkpoint = form.checkpoint_number.data
        return render_template('moving_user.html', title='Move User', form=form)


# current_session = requests.session()
# current_session.get('/')