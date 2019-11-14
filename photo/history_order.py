from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from photo.auth import login_required
from photo.db import get_db

bp = Blueprint('history_order', __name__)

@bp.route('/history_order/history_index')
def history_index():
    if (g.user):
        g.current = "history_order.history_index"
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "SELECT *"
            " FROM porder"
            " WHERE status = 'complete'"
            " ORDER BY satisfaction DESC"
        )
        orders = cursor.fetchall()
        return render_template('history_order/history_index.html', orders=orders)
    else:
        return redirect(url_for('auth.login'))


