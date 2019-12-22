from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from fifa.db import get_db

bp = Blueprint('team_detail', __name__)

@bp.route('/<int:id>/team_detail')
def index(id):
    g.current = "team_detail"
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
    "SELECT p.id id, p.photo photo, p.name name, n.flag flag, n.nationality nationality, p.position position,p.value value, p.wage wage, p.overall overall, p.potential potential"
    " FROM player p, nation n "
    " WHERE p.nation_id = n.nation_id AND club_id = %s", id
)
    players = cursor.fetchall()
    for player in players:
        player["value"] = '%.1f' % (player["value"])
    cursor.execute(
        "SELECT club_name, club_logo"
        " FROM team"
        " WHERE club_id = %s", id
    )
    club_name = cursor.fetchone()

    cursor.execute(
    "SELECT *"
    " FROM player0"
    " WHERE club_id = %s", id
)
    attributes = cursor.fetchall()

    cursor.execute(
        "SELECT *"
        " FROM team"
        " WHERE club_id = %s", id
    )
    team_attribute = cursor.fetchone()
    team_attribute["overall"]=int(team_attribute["overall"])
    team_attribute["potential"]=int(team_attribute["potential"])
    team_attribute["totalvalue"]='%.1f'%(team_attribute["totalvalue"])
    team_attribute["totalwage"]=int(team_attribute["totalwage"])
    return render_template('team_detail.html', players = players, club_name = club_name, attributes = attributes, team_attribute = team_attribute)

