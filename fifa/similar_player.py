from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, Response, request, jsonify,json
)
from werkzeug.exceptions import abort
from werkzeug.security import check_password_hash, generate_password_hash

# from photo.auth import login_required
from fifa.db import get_db

bp = Blueprint('similar_player', __name__)



@bp.route('/<int:id>/similar_player_score')
def player_score(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "SELECT pace_score,shooting_score,passing_score,dribbling_score,defending_score,physical_score"
        " FROM rating"
        " WHERE ID = %s",id
    )
    player = cursor.fetchone()
    player_score = []
    for key in player:
        player_score.append(player[key])
    return  jsonify(player_score)


@bp.route('/<int:id>/similar_player', methods=('GET', 'POST'))
def index(id):
    g.current = "player"
    db = get_db()
    cursor = db.cursor()
    # cursor.execute(
    # "SELECT *"
    # " FROM recommend "
    # " WHERE recommend.ID = %s", id
    # )
    # data = cursor.fetchone()

    # for key in data:
    #     if key.lower() != "id"
    #     player_score.append(player[key])  
    cursor.execute(
    "SELECT p.id id, p.photo photo, p.name name, n.flag flag, n.nationality nationality, p.value value, p.wage wage, p.overall overall, p.potential potential"
    " FROM player p, nation n, recommend re"
    " WHERE p.nation_id = n.nation_id AND p.id = re.id AND (p.ID = re.sp1_id OR p.ID = re.sp2_id, OR p.ID = re.sp3_id, OR p.ID = re.sp4_id, OR p.ID = re.sp5_id)"
    )

    similar_players = cursor.fetchall()
    return render_template('similar_player.html', id = id, similar_players = similar_players)