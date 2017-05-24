from flask import Flask
from flask_bootstrap import Bootstrap
from api import bp_api
from admin import bp_admin

bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)

    bootstrap.init_app(app)

    app.register_blueprint(bp_api, url_prefix='/api')
    app.register_blueprint(bp_admin, url_prefix='/admin')

    return app
