from flask import Flask, render_template, redirect, request, url_for, flash
from . import bp_api


@bp_api.route('/order')
def index():
    print '__name__', __name__
    return render_template('api/index.html', subtitle='API.:|')

