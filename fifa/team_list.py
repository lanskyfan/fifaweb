from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

# from photo.auth import login_required
from fifa.db import get_db

bp = Blueprint('team_list', __name__)

@bp.route('/team_list')
def team_index():
    if (g.user):
        g.current = "team_list.history_index"
        db = get_db()
        cursor = db.cursor()
        # cursor.execute(
        #     "SELECT *"
        #     " FROM porder"
        #     " WHERE status = 'complete'"
        #     " ORDER BY satisfaction DESC"
        # )
        # orders = cursor.fetchall()
        return render_template('team_list.html')
    else:
        return redirect(url_for('auth.login'))


