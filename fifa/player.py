from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, Response, request, jsonify,json
)
from werkzeug.exceptions import abort
from werkzeug.security import check_password_hash, generate_password_hash

# from photo.auth import login_required
from fifa.db import get_db

bp = Blueprint('player', __name__)
# @bp.route('/player/index', methods=('GET', 'POST'))



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
    # cursor.execute(
    #     "SELECT pace_score,shooting_score,passing_score,dribbling_score,defending_score,physical_score,GK_score"
    #     " FROM rating"
    #     " WHERE ID = 231747"
    # )
    # player = cursor.fetchone()

    # cursor.execute("SELECT phone FROM %s_phone WHERE id = '%d'" % (position, id,))
    # phone = cursor.fetchone()
    # if phone == None:
    #     cursor.execute("SELECT pos.id, pos.position position, pos.username username, pos.level level, "
    #     "pos.birthday birthday, pos.home home"
    #     " FROM %s pos"
    #     " WHERE pos.id = '%d'" % (position, id,))
    #     players = cursor.fetchone()
    #     players['phone'] = None
    # else:
    #     cursor.execute("SELECT pos.id, pos.position position, pos.username username, pos.level level, "
    #             "pos.birthday birthday, pos.home home, MAX(phone.phone) phone"
    #             " FROM %s pos, %s_phone phone"
    #             " WHERE pos.id = '%d' AND"
    #             " pos.id = phone.id" % (position, position, id,))
    #     players = cursor.fetchone()

    return render_template('player.html', id = id, player_detail = player_detail)

# def get_player(id, position, check_author=True):   
#     db = get_db()
#     cursor = db.cursor()
#     # position = "".join(position.split()) ## remove space
#     sql = ("SELECT * FROM %s WHERE id = '%d'" % (position, id,))
#     cursor.execute(sql)
#     players = cursor.fetchone()
    
#     cursor.execute("SELECT phone FROM %s_phone WHERE id = '%d'" % (position, id,))
#     phone = cursor.fetchone()
#     if phone == None:
#         players['phone'] = None
#     else:
#         players['phone'] = phone['phone']
    
#     if players is None:
#         abort(404, "Post id {0} doesn't exist.".format(id))

#     if check_author and players['id'] != g.user['id']:
#         abort(403)

#     return players

# @bp.route('/<int:id>/<string:position>/player/update', methods=('GET', 'POST'))
# @login_required
# def update(id, position):
#     g.current = "player"
#     players = get_player(id, position)
#     if players['position'] == 'aftereffect':
#         players['position'] = 'After Effect'
#     if players['position'] == 'devicemanager':
#         players['position'] = 'Device Manager'
#     if players['position'] == 'projectmanager':
#         players['position'] = 'Project Manager'
#     if players['position'] == 'photographer':
#         players['position'] = 'Photographer'

#     if request.method == 'POST':
#         username = request.form['username']
#         birthday = request.form['birthday']
#         phone = request.form['phone']
#         password = request.form['password']
#         password2 = request.form['password2']
#         home = request.form['address']
#         username = str(username)
#         birthday = str(birthday)
#         phone = str(phone)
#         password = str(password)
#         password2 = str(password2)
#         error = None


#         if not username:
#             error = 'Username is required.'
#         if password != password2:
#             error = 'Password is not consistent'
#         if not (len(phone) == 11 or len(phone) == 8) or not phone.isdigit():
#             error = 'Incorrect phone'
        
#         if error is not None:
#             flash(error)
#             return render_template('player/player_update.html', players=players, error = error)
#         else:

#             db = get_db()
#             cursor = db.cursor()
#             cursor.execute("DELETE FROM %s_phone WHERE id = '%d'" % (position, id))
#             cursor.execute(
#                 "UPDATE %s SET username = '%s', birthday = '%s', password = '%s', home = '%s'"
#                 " WHERE id = '%d'" % \
#                 (position, username, birthday, generate_password_hash(password), home, id)
#             )
#             cursor.execute("INSERT INTO %s_phone(id, phone) VALUES ('%d', '%s')" % (position, id, phone))
#             db.commit()
#             return redirect(url_for('player.index', id=id, position=position))
#         return render_template('player/player_update.html', players=players, error = error)
#     return render_template('player/player_update.html', players=players)

# @bp.route('/<int:id>/player/delete', methods=('POST',))
# @login_required
# def delete(id):
#     position = 'photographer' # just in case
#     g.current = "player"
#     get_player(id, position)
#     db = get_db()
#     cursor = db.cursor()
#     cursor.execute("DELETE FROM post WHERE id = '%d'" % (id,))
#     db.commit()
#     return redirect(url_for('dashboard.index'))