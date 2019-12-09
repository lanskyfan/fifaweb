from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from fifa.db import get_db

bp = Blueprint('player_list', __name__)

@bp.route('/player_list', methods=('GET', 'POST'))
def player_index():
    g.current = "player_list"
    db = get_db()
    cursor = db.cursor()
    players = None
    error = None
    if request.method == 'POST':
        player_name = request.form['player_name']
        player_name = str(player_name)
        player_name = player_name.lower()
        error = None
        if not player_name:
            error = 'Basic information is not complete.'

        cursor.execute(
        "SELECT p.id id, p.age age, p.photo photo, p.name name, p.position position, n.flag flag, n.nationality nationality, p.value value, p.wage wage, p.overall overall, p.potential potential"
        " FROM player p, nation n "
        " WHERE p.nation_id = n.nation_id AND LOWER(p.name) LIKE %s", ("%"+ player_name + "%")
        )
        players = cursor.fetchall()
        if players is None:
            error = 'Player not found'
            return render_template('player_list.html', players = players)

        else:
            flash(error)
            for player in players:
                player["value"] = '%.1f' % (player["value"])
            return render_template('player_list.html', players = players)

    else: 
        cursor.execute(
        "SELECT p.id id, p.age age, p.photo photo, p.name name, p.position position, n.flag flag, n.nationality nationality, p.value value, p.wage wage, p.overall overall, p.potential potential"
        " FROM player p, nation n "
        " WHERE p.nation_id = n.nation_id"
        " ORDER BY p.overall desc LIMIT 50"
        )
        players = cursor.fetchall()
        for player in players:
            player["value"] = '%.1f' % (player["value"])
            
        return render_template('player_list.html', players = players)


