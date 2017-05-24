from flask import Flask, render_template, redirect, request, url_for, flash
from . import bp_admin


@bp_admin.route('/admin')
def index():
    print '__name__', __name__
    return render_template('admin.html')
