import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from ..database.db import db

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
    result = db.engine.execute(
            "select * from barang")
    aData = [{"id": row[0], "kode_barang":row[1],
                  "nama_barang":row[2], "harga":row[3], "stok":row[4]} for row in result]
    data = {
            "message": "Get all barang",
            "aData": aData
        }

    return data, 200, {'ContentType': 'application/json'}