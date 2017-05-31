from flask import Blueprint

bp_wx = Blueprint('wx', __name__)

from . import views

