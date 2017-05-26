# -*- coding: utf-8 -*-
# from flask.ext.wtf import FlaskForm
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Length


class MyForm1(FlaskForm):
    name = StringField('Names?',
                       validators=[DataRequired('you dont have name?')],
                       description='your name here',
                       render_kw={'placeholder': 'What\'s your name'})
    pwds = PasswordField('Password', validators=[DataRequired(), EqualTo('cnfm', message='Password not match')])
    cnfm = PasswordField('Confirm Password')
    onoff = BooleanField('Choose')
    submit = SubmitField('Enter')


class RegistrationForm(FlaskForm):
    """用户注册"""
    username = StringField('Username', validators=[Length(min=4, max=25)], render_kw={'placeholder': 'username'})
    email = StringField('Email Address', validators=[Length(min=6, max=35)], render_kw={'placeholder': 'email address'})
    password = PasswordField('New Password', validators=[DataRequired(),
                                                         EqualTo('confirm', message='Passwords must match')],
                             render_kw={'placeholder': 'password'})
    confirm = PasswordField('Confirm Password', validators=[DataRequired()],
                            render_kw={'placeholder': 'confirm password'})
    # accept_tos = BooleanField('I accept the TOS', validators=[DataRequired('Need Check')])
    submit = SubmitField('Register!')


class LoginForm(FlaskForm):
    """用户登陆"""
    username = StringField('Username', validators=[Length(min=4, max=25)], render_kw={'placeholder': 'username'})
    password = PasswordField('New Password', validators=[DataRequired()], render_kw={'placeholder': 'password'})
    remember = BooleanField('Remember', validators=[DataRequired()])
    submit = SubmitField('Login')


