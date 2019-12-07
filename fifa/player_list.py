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
    "SELECT p.id id, p.photo photo, p.name name, p.position position, n.flag flag, n.nationality nationality, p.value value, p.wage wage, p.overall overall, p.potential potential"
    " FROM player p, nation n "
    " WHERE p.nation_id = n.nation_id"
    )
    players = cursor.fetchall()
    for player in players:
        player["value"] = '%.1f' % (player["value"])
        
    return render_template('player_list.html', players = players)


