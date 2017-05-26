from . import db


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    rolename = db.Column(db.String(64), unique=True)
    permission = db.Column(db.Integer)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64))
    password = db.Column(db.String(64))
    signuptime = db.Column(db.DateTime())
    logintime = db.Column(db.DateTime())


