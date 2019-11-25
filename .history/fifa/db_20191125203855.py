import pymysql
import os
import click
from flask import current_app, g
from flask.cli import with_appcontext

def parse_sql(filename):
    data = open(filename, 'r').readlines()
    stmts = []
    DELIMITER = ';'
    stmt = ''

    for lineno, line in enumerate(data):
        if not line.strip():
            continue

        if line.startswith('--'):
            continue

        if 'DELIMITER' in line:
            DELIMITER = line.split()[1]
            continue

        if (DELIMITER not in line):
            stmt += line.replace(DELIMITER, ';')
            continue

        if stmt:
            stmt += line
            stmts.append(stmt.strip())
            stmt = ''
        else:
            stmts.append(line.strip())
    return stmts

def get_db():
    if 'db' not in g:
        g.db = pymysql.connect(host='localhost',
                               user='photodev',
                               port=3306,
                               password='123456',
                               db='photo',
                               charset='utf8mb4',
                               conv=pymysql.converters.conversions,
                               cursorclass=pymysql.cursors.DictCursor)

           
        # g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()
    cursor = db.cursor()
    DATABASE=os.path.join(os.path.dirname(__file__), 'schema_order.sql')
    stmts = parse_sql(DATABASE)
    for stmt in stmts:
        cursor.execute(stmt)
    
    db.commit()
    INSERTION=os.path.join(os.path.dirname(__file__), 'insert.sql')
    insts = parse_sql(INSERTION)
    for inst in insts:
        cursor.execute(inst)
    db.commit()



@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
