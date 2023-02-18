from flask import Flask, render_template, current_app
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_admin.contrib.sqla import ModelView
import flask_wtf
from config import Config
from app import routes


app = Flask(__name__)
engine = create_engine("sqlite:///DataBase/ONboard.db/ONboard.db", echo=True)

app.config['FLASK_ADMIN_SWATCH'] = "Cosmo"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ONboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config.from_object(Config)

db = SQLAlchemy(app)

with app.app_context():
    print(current_app.name)


@app.get('/')
def index():
    return render_template('adminka.html')


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    surname = db.Column(db.String(20), unique=False, nullable=False)
    lastname = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(20), nullable=False)
    last_seen = db.Column(db.DateTime)
    user_status = db.Column(db.String(40), nullable=True, default='Новый сотрудник')
    user_achievements = db.Column(db.String(), nullable=, default='Новый сотрудник')

class Tests(db.Model):
    __tablename__ = 'tests'
    id = db.column(db.Integer, primary_key=True)


# class HR(db.Model):
#     __tablename__ = "user"
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=False, nullable=False)
#     email = db.Column(db.String(120), unique=False, nullable=False)
#     image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
#     password = db.Column(db.String(60), nullable=False)
#     last_seen = db.Column(db.DateTime)
#     user_status = db.Column(db.String(40), nullable=True, default='Лучший пользователь проекта')


admin = Admin(app, name='', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session, name='Пользователь'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
