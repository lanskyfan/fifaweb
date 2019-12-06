from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

# from photo.auth import login_required
from fifa.db import get_db

bp = Blueprint('team_list', __name__)

@bp.route('/team_list')
def team_index():
    g.current = "team_list"
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "SELECT *"
        " FROM team"
    )
    teams = cursor.fetchall()
    for i in range(650):
        teams[i]["overall"]=int(teams[i]["overall"])
        teams[i]["potential"]=int(teams[i]["potential"])
        teams[i]["totalvalue"]='%.1f'%(teams[i]["totalvalue"])
        teams[i]["totalwage"]=int(teams[i]["totalwage"])
    return render_template('team_list.html', teams = teams)


