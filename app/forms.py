from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class UsermoveForm(FlaskForm):
    user_id = IntegerField('Id пользователя', validators=[DataRequired()])
    checkpoint_number = IntegerField('Нужный чекпоинт', validators=[DataRequired()])
    submit = SubmitField('Готово')
