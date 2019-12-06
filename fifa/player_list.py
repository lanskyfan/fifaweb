from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from fifa.db import get_db

bp = Blueprint('player_list', __name__)

@bp.route('/player_list')
def team_index():
    g.current = "player_list"
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "SELECT *"
        " FROM player"
    )
    players = cursor.fetchall()
    return render_template('player_list.html', players = players)


