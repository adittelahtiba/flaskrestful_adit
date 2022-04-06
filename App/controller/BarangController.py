import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

# from flaskr.db import get_db
from ..database.db import tes

bp = Blueprint('BarangController', __name__, url_prefix='/barang')

@bp.route('', methods=('GET', 'POST'))
def register():
    data=None
    if request.method == 'POST':
        
        return "post"
        # username = request.form['username']
        # password = request.form['password']
        # db = get_db()
        # error = None

        # if not username:
        #     error = 'Username is required.'
        # elif not password:
        #     error = 'Password is required.'

        # if error is None:
        #     try:
        #         db.execute(
        #             "INSERT INTO user (username, password) VALUES (?, ?)",
        #             (username, generate_password_hash(password)),
        #         )
        #         db.commit()
        #     except db.IntegrityError:
        #         error = f"User {username} is already registered."
        #     else:
        #         return redirect(url_for("auth.login"))

        flash(error)
    data=tes()
    return data, 200, {'ContentType': 'application/json'}