from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config

# blueprint
from main import bp_main
from api import bp_api
from admin import bp_admin


bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)

    app.register_blueprint(bp_main, url_prefix='/')
    app.register_blueprint(bp_api, url_prefix='/api')
    app.register_blueprint(bp_admin, url_prefix='/admin')

    return app
