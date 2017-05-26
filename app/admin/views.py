from flask import session
from flask import request
from flask import render_template, render_template_string
from flask import redirect
from flask import url_for
from flask import flash
from . import bp_admin
from .forms import MyForm1, RegistrationForm, LoginForm


@bp_admin.route('/')
def index():
    print __name__
    return render_template('admin/admin.html')


@bp_admin.route('/testform', methods=['GET', 'POST'])
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

    return render_template('admin/form.html', form=form, name=session.get('name'), pwds=session.get('pwds'), onoff=session.get('onoff'))


@bp_admin.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if request.method == 'POST' and form.validate_on_submit():
        print 'got:', form.username.data, form.email.data, form.password.data, form.confirm.data

        flash('Thanks for registering')

        return redirect(url_for('main.index'))
    print 'render_template'
    # flash('render_template')
    return render_template('admin/register.html', form=form)


@bp_admin.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        print 'got:', form.username.dataform.password.data, form.remember.data

        flash('Thanks for login')

        return redirect(url_for('main.index'))
    print 'render_template'
    # flash('render_template')

    return render_template('admin/login.html', form=form)



