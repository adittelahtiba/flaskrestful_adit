import os

from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .database import db
    db.db_con(app)

    from .controller import UserController, BarangController
    app.register_blueprint(UserController.bp)
    app.register_blueprint(BarangController.bp)

    return app
