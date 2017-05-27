# -*- coding: utf-8 -*-
from flask import session, request, render_template, redirect, url_for, flash
from . import bp_auth
from .forms import MyForm1, RegistrationForm, LoginForm
from .. import db
from ..models import User
from flask_login import login_required, login_user, logout_user


@bp_auth.route('/')
def index():
    print __name__
    return render_template('auth/index.html')


@bp_auth.route('/register', methods=['GET', 'POST'])
def register():
    print __name__
    form = RegistrationForm()

    if request.method == 'POST' and form.validate_on_submit():
        print 'got:', form.username.data, form.email.data, form.password.data, form.confirm.data
        newuser = User(username=form.username.data, password=form.password.data, email=form.email.data)
        db.session.add(newuser)
        flash('Thanks for registering')

        return redirect(url_for('main.index'))

    return render_template('auth/register.html', form=form, subtitle=u'注册')


@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    print __name__

    form = LoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        print 'got:', form.username.data, form.password.data

        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            # 跳转到登陆之差的页面或首页
            return redirect(request.args.get('next') or url_for('main.index'))

        flash(u'用户名或密码错误，请重新登陆.')

    return render_template('auth/login.html', form=form, subtitle=u'登陆')


@bp_auth.route('/logout')
def logout():
    print __name__

    logout_user()
    flash('Logout success!')
    return render_template('test_show.html', detail='Logout success. Welcome back.')


@bp_auth.route('/authonly')
@login_required
def authonly():
    print __name__

    return render_template('test_show.html', detail='Auth Only View')


@bp_auth.route('/anyone')
def anybody():
    print __name__

    return render_template('test_show.html', detail='Andybody View')




# @bp_auth.route('/testform', methods=['GET', 'POST'])
# def myform():
#     print __name__
#     # username = None
#     # password = None
#     # onoff = None
#     form = MyForm1()
#
#     print 'Befor:', form.username.data, form.pwds.data, form.onoff.data
#
#     if form.validate_on_submit():
#         # username = form.username.data
#         # password = form.pwds.data
#         # onoff = form.onoff.data
#         print 'got:', form.username.data, form.pwds.data, form.onoff.data
#
#         if session.get('username') == form.username.data and form.username.data is not None:
#             flash('hey, c u again.')
#
#         session['username'] = form.username.data
#         session['pwds'] = form.pwds.data
#         session['onoff'] = form.onoff.data
#
#         print url_for('auth.myform')
#
#         return redirect(url_for('auth.myform'))
#
#         # form.username.data = ''
#         # form.pwds.data = ''
#         # form.onoff.data = False
#     else:
#         # flash(form.username.errors[0])
#         print 'E1', form.username.errors
#         # print 'E2', form.pwds.errors
#
#     return render_template('auth/form.html', form=form, username=session.get('username'), pwds=session.get('pwds'), onoff=session.get('onoff'))

