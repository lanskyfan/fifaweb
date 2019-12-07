from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

# from photo.auth import login_required
from fifa.db import get_db

bp = Blueprint('dashboard', __name__)

@bp.route('/', methods=('GET', 'POST'))
def index():
    # Here we need to implement an algorithm to select the team to display
    g.current = "dashboard"
    db = get_db()
    cursor = db.cursor()

    teams = None
    players = None
    error = None
    if request.method == 'POST':
        team_name = request.form['team_name']
        team_name = str(team_name)
        team_name = team_name.lower()
        player_name = request.form['player_name']
        player_name = str(player_name)
        player_name = player_name.lower()
        error = None
        if not team_name:
            error = 'Basic information is not complete.'

        # val = (team_name,)
        cursor.execute("SELECT * FROM team WHERE LOWER(club_name) LIKE %s" , ("%"+team_name+"%",))
        teams = cursor.fetchall()
        cursor.execute(
        "SELECT p.id id, p.photo photo, p.name name, p.position position, n.flag flag, n.nationality nationality, p.value value, p.wage wage, p.overall overall, p.potential potential"
        " FROM player p, nation n "
        " WHERE p.nation_id = n.nation_id AND LOWER(p.name) LIKE %s", ("%"+ player_name + "%")
        )
        players = cursor.fetchall()
        if teams is None and players is not None:
            for player in players:
                player["value"] = '%.1f' % (player["value"])
            return render_template('player_list.html', players = players)

        elif teams is not None and players is None:
            for i in range(len(teams)):
                teams[i]["overall"]=int(teams[i]["overall"])
                teams[i]["potential"]=int(teams[i]["potential"])
                teams[i]["totalvalue"]='%.1f'%(teams[i]["totalvalue"])
                teams[i]["totalwage"]=int(teams[i]["totalwage"])
            return render_template('team_list.html', teams=teams)
        else:
            return render_template('index.html')

    else:
        return render_template('index.html')
    # return render_template('base.html')

