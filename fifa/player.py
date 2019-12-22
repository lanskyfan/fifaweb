from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, Response, request, jsonify,json
)
from werkzeug.exceptions import abort
from werkzeug.security import check_password_hash, generate_password_hash

from fifa.db import get_db

bp = Blueprint('player', __name__)


@bp.route('/<int:id>/score')
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

@bp.route('/<int:id>/passing')
def passing_func(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "SELECT vision, crossing, FK_accuracy, short_passing, long_passing, curve"
        " FROM passing"
        " WHERE ID = %s", id
    )
    passing = cursor.fetchone()
    passing_list = []
    for key in passing:
        passing_list.append(passing[key])
    return jsonify(passing_list)

@bp.route('/<int:id>/shooting')
def shooting_func(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "SELECT positioning, finishing, shot_power, long_shots, volleys, penalties"
        " FROM shooting"
        " WHERE ID = %s", id
    )
    shooting = cursor.fetchone()
    shooting_list = []
    for key in shooting:
        shooting_list.append(shooting[key])
    return jsonify(shooting_list)

@bp.route('/<int:id>/defending')
def defending_func(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "SELECT interceptions, headingaccuracy, marking, standing_tackle, sliding_tackle"
        " FROM defending"
        " WHERE ID = %s", id
    )
    defending = cursor.fetchone()
    defending_list = []
    for key in defending:
        defending_list.append(defending[key])
    return jsonify(defending_list)


@bp.route('/<int:id>/dribbling2')
def dribbling2_func(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "SELECT agility, balance, reactions, ball_control, dribbling,composure"
        " FROM dribbling2"
        " WHERE ID = %s", id
    )
    dribbling2 = cursor.fetchone()
    dribbling2_list = []
    for key in dribbling2:
        dribbling2_list.append(dribbling2[key])
    return jsonify(dribbling2_list)
    
@bp.route('/<int:id>/physical')
def physical_func(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "SELECT jumping, stamina, strength, aggression"
        " FROM physical"
        " WHERE ID = %s", id
    )
    physical = cursor.fetchone()
    physical_list = []
    for key in physical:
        physical_list.append(physical[key])
    return jsonify(physical_list)

@bp.route('/<int:id>/gk')
def gk_func(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "SELECT GK_handling, GK_kicking, GK_positioning, GK_reflexes"
        " FROM GK"
        " WHERE ID = %s", id
    )
    gk = cursor.fetchone()
    gk_list = []
    for key in gk:
        gk_list.append(gk[key])
    return jsonify(gk_list)

@bp.route('/<int:id>/player', methods=('GET', 'POST'))
def index(id):
    g.current = "player"
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
    "SELECT p.id id, p.age age,p.club_id club_id, p.photo photo, p.name name, p.position position, n.flag flag, n.nationality nationality, p.value value, p.wage wage, p.overall overall, p.potential potential, c.club_name club_name, c.club_logo logo"
    " FROM player p, nation n, team c "
    " WHERE p.nation_id = n.nation_id AND p.club_id=c.club_id AND p.id = %s", id
    )
    player_detail = cursor.fetchone()
    player_detail["value"] = '%.1f' % (player_detail["value"])
    return render_template('player.html', id = id, player_detail = player_detail)