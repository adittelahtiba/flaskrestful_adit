import click
from flask import current_app, g, Flask
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
import os


def db_con():
    app = Flask(__name__, instance_relative_config=True)
    app.config['SECRET_KEY'] = 'hardsecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@localhost/gudang_wahaji'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(app)
    
    return db


def tes():
    db=db_con()
    result = db.engine.execute(
            "select * from barang")
    
    return result

