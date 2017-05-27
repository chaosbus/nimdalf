# -*- coding: utf-8 -*-
# from flask.ext.wtf import FlaskForm
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Length


class MyForm1(FlaskForm):
    name = StringField('Names?',
                       validators=[DataRequired('you dont have username?')],
                       description='your username here',
                       render_kw={'placeholder': 'What\'s your username'})
    pwds = PasswordField('Password', validators=[DataRequired(), EqualTo('cnfm', message='Password not match')])
    cnfm = PasswordField('Confirm Password')
    onoff = BooleanField('Choose')
    submit = SubmitField('Enter')


class RegistrationForm(FlaskForm):
    """用户注册"""
    username = StringField('Username', validators=[Length(min=4, max=25)], render_kw={'placeholder': u'请输入帐号'})
    email = StringField('Email Address', validators=[Length(min=6, max=35)], render_kw={'placeholder': u'请输入邮箱'})
    password = PasswordField('New Password', validators=[DataRequired(),
                                                         Length(min=4, max=32),
                                                         EqualTo('confirm', message=u'密码不一致')],
                             render_kw={'placeholder': u'请输入密码'})
    confirm = PasswordField('Confirm Password', validators=[DataRequired()],
                            render_kw={'placeholder': u'请输入相同的密码'})
    # accept_tos = BooleanField('I accept the TOS', validators=[DataRequired('Need Check')])
    submit = SubmitField(u'注册')


class LoginForm(FlaskForm):
    """用户登陆"""
    username = StringField('Username', validators=[Length(min=4, max=25)], render_kw={'placeholder': u'请输入帐号'})
    password = PasswordField('New Password', validators=[DataRequired()], render_kw={'placeholder': u'请输入密码'})
    remember_me = BooleanField('Keep logged in')
    submit = SubmitField(u'登陆')


