import os
import pymysql
from flaskext.mysql import MySQL
from decouple import config

mysql = MySQL()

def init_db(app):
    app.config['MYSQL_DATABASE_HOST'] = config('MYSQL_HOST', default='localhost')
    app.config['MYSQL_DATABASE_PORT'] = config('MYSQL_PORT', default=3306, cast=int)  
    app.config['MYSQL_DATABASE_USER'] = config('MYSQL_USER', default='root')
    app.config['MYSQL_DATABASE_PASSWORD'] = config('MYSQL_PASSWORD', default='')
    app.config['MYSQL_DATABASE_DB'] = config('MYSQL_DB', default='sistema')

    mysql.init_app(app)  

def get_connection():
    try:
        return pymysql.connect(
            host=config('MYSQL_HOST', default='localhost'),
            port=config('MYSQL_PORT', default=3306, cast=int),
            user=config('MYSQL_USER', default='root'),
            password=config('MYSQL_PASSWORD', default=''),
            db=config('MYSQL_DB', default='sistema'),
            cursorclass=pymysql.cursors.DictCursor
        )
    except Exception as ex:
        return None  