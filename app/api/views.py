from flask import Flask, render_template, redirect, request, url_for, flash
from . import bp_api
from .. import db
from ..models import SubsOperation

@bp_api.route('/')
def index():
    print '__name__', __name__
    return render_template('api/index.html', subtitle='API::')


@bp_api.route('/aqi')
def aqi():
    print '__name__', __name__
    return render_template('api/aqi.html', subtitle='AQI Stats')


@bp_api.route('/pi')
def pi():
    print '__name__', __name__
    return render_template('api/pi.html', subtitle='RaspberryPi')


@bp_api.route('/show')
def show():
    dat = SubsOperation.query.all()
    print SubsOperation.query.count()

    return render_template('api/show.html', table=dat)