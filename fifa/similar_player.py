from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, Response, request, jsonify,json
)
from werkzeug.exceptions import abort
from werkzeug.security import check_password_hash, generate_password_hash

# from photo.auth import login_required
from fifa.db import get_db

bp = Blueprint('similar_player', __name__)



@bp.route('/<int:id_old>/<int:id_new>/similar_player_score')
def player_score(id_old, id_new):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "SELECT p.name name, r.pace_score pace_score,r.shooting_score shooting_score, r.passing_score passing_score, r.dribbling_score dribbling_score, r.defending_score defending_score, r.physical_score physical_score"
        " FROM player p, rating r"
        " WHERE p.ID = r.ID AND r.ID = %s",id_old
    )
    old_player = cursor.fetchone()
    player_score_old = []
    for key in old_player:
        player_score_old.append(old_player[key])

    cursor.execute(
        "SELECT p.name name, r.pace_score pace_score,r.shooting_score shooting_score,r.passing_score passing_score, r.dribbling_score dribbling_score, r.defending_score defending_score, r.physical_score physical_score"
        " FROM player p, rating r"
        " WHERE p.ID = r.ID AND r.ID = %s",id_new
    )
    new_player = cursor.fetchone()
    player_score_new = []
    for key in new_player:
        player_score_new.append(new_player[key])

    player_score_all = [player_score_old, player_score_new]
    return  jsonify(player_score_all)


@bp.route('/<int:id>/similar_player', methods=('GET', 'POST'))
def index(id):
    g.current = "player"
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
    "SELECT *"
    " FROM recommend "
    " WHERE recommend.ID = %s", id
    )
    data = cursor.fetchone()

    players = []
    for key in data:
        players.append(data[key])
            
    similar_players = []
    for player in players:
        cursor.execute(
        "SELECT p.id id,p.age age, p.club_id club_id, p.photo photo, p.name name, p.position position, n.flag flag, n.nationality nationality, p.value value, p.wage wage, p.overall overall, p.potential potential, t.club_name club_name, t.club_logo logo"
        " FROM player p, nation n , team t"
        " WHERE p.nation_id = n.nation_id AND p.club_id=t.club_id AND p.id = %s", player
        )
        similar_player = cursor.fetchone()
        similar_player["value"] = '%.1f' % (similar_player["value"])
        similar_players.append(similar_player)

    return render_template('similar_player.html', id = id, similar_players = similar_players)