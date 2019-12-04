from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

# from photo.auth import login_required
from fifa.db import get_db

bp = Blueprint('team_list', __name__)

@bp.route('/team_list')
def team_index():
    g.current = "team_list.history_index"
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "SELECT player.club_id, club.club_name club_name ,club.logo club_logo,count(*) count,avg(overall) overall, avg(potential) potential,sum(Value) value, sum(Wage) wage"
        " FROM player, club"
        " WHERE player.club_id = club.club_id"
        " GROUP BY club_id;"
    )
    teams = cursor.fetchall()
    return render_template('team_list.html', teams = teams)


