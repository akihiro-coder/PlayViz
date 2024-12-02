"""
setup our baseball_app
"""

import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import load_config



def create_app():

    # define app of Flask
    app = Flask(__name__, template_folder='./templates', static_folder='./static')

    # load config
    app.config.from_object(load_config())

    # init SQLAlchemy so we can use it later in our models
    db = SQLAlchemy(app)

    # init database
    db.init_app(app)

    # create database migration engine
    migrate = Migrate(app, db)

    # baseball_appディレクトリをモジュール検索パスに追加
    # add baseball_app dir to module search path
    sys.path.append(os.path.dirname(__file__))

    # register Blueprint
    from controllers.auth.route import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app