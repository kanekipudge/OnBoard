from app import db
from flask_login import UserMixin
from app import login
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False)
    surname = db.Column(db.String(20), unique=False)
    lastname = db.Column(db.String(20), unique=False)
    email = db.Column(db.String(120), unique=True)
    phone_number = db.Column(db.String(120), unique=True)
    rating = db.Column(db.Integer, unique=False)
    password = db.Column(db.String(128))
    role = db.Column(db.String(10), unique=False)
    checkpoint_current = db.Column(db.Integer, unique=False, default=1)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    # def set_password(self, password):
    #     self.password_hash = generate_password_hash(password)
    #
    # def check_password(self, password):
    #     return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# class Tests(db.Model):
#     user_id = db.Column(db.ForeignKey('User.id'))
#     checkpoint1 = db.Column(db.Integer)
