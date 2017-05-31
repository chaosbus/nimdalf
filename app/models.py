# -*- coding: utf-8 -*-
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from . import login_manager


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    permission = db.Column(db.Integer)

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))
    signup_time = db.Column(db.DateTime())
    login_time = db.Column(db.DateTime())

    @property
    def password(self):
        raise AttributeError('Password is not readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return True

    def get_id(self):
        return unicode(self.id)


@login_manager.user_loader
def load_user(user_id):
    """
    Flasg_Login用于标识加载用户
    :param user_id:
    :return:
    """
    return User.query.get(int(user_id))


class SubsOperation(db.Model):
    __name__ == 'subsoperation'

    id = db.Column(db.Integer, primary_key=True)
    product_code = db.Column(db.String(21))
    user_msisdn = db.Column(db.String(48))
    pay_user = db.Column(db.String(48))
    operation = db.Column(db.String(2))
    status = db.Column(db.String(2))
    operation_mode = db.Column(db.Integer)
    operation_date = db.Column(db.DateTime)
    effictive_date = db.Column(db.DateTime)
    device_type = db.Column(db.Integer)
    device_id = db.Column(db.String(6))

    def __repr__(self):
        return '<SubsOperation %r>' % self.id

