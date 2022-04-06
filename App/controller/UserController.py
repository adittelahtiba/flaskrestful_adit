import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

# db
bp = Blueprint('UserController', __name__, url_prefix='/')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.json['username']
        password = request.json['password']

        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."

        flash(error)
    
    return request.json, 200, {'ContentType': 'application/json'}


@bp.route('/user', methods=('GET', 'POST'))
def hello():    
    result = db.engine.execute("select * from user")
    aData = [{"username": row[1], "password":row[2]} for row in result]
    data = {
        "message": "Get all user",
        "aData": aData
    }
    return data, 200, {'ContentType': 'application/json'}
