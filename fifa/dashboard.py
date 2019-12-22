from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from fifa.db import get_db

bp = Blueprint('dashboard', __name__)

@bp.route('/', methods=('GET', 'POST'))
def index():
    g.current = "dashboard"
    return render_template('index.html')

