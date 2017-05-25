# -*- coding: utf-8 *-*
from flask import session
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for
from flask import flash
from flask.ext.wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateField, BooleanField
from wtforms.validators import DataRequired, Required
from . import bp_admin


@bp_admin.route('/')
def index():
    print '__name__', __name__
    return render_template('admin.html')


class MyForm1(FlaskForm):
    name = StringField('Names?', validators=[DataRequired('you dont have name?')])
    pwds = PasswordField('Password')
    today = DateField('TimeNow')
    onoff = BooleanField('Choose')
    submit = SubmitField('Enter')


@bp_admin.route('/form1', methods=['GET', 'POST'])
def myform():
    print __name__
    # name = None
    # password = None
    # onoff = None
    form = MyForm1()

    print 'Befor:', form.name.data, form.pwds.data, form.onoff.data

    if form.validate_on_submit():
        # name = form.name.data
        # password = form.pwds.data
        # onoff = form.onoff.data
        print 'got:', form.name.data, form.pwds.data, form.onoff.data

        if session.get('name') == form.name.data and form.name.data is not None:
            flash('hey, c u again.')

        session['name'] = form.name.data
        session['pwds'] = form.pwds.data
        session['onoff'] = form.onoff.data

        print url_for('admin.myform')

        return redirect(url_for('admin.myform'))

        # form.name.data = ''
        # form.pwds.data = ''
        # form.onoff.data = False
    else:
        # flash(form.name.errors[0])
        print 'E1', form.name.errors
        # print 'E2', form.pwds.errors

    return render_template('form.html', form=form, name=session.get('name'), pwds=session.get('pwds'), onoff=session.get('onoff'))
