from decouple import config
import pymysql
from flaskext.mysql import MySQL

mysql = MySQL()

def init_db(app):

    app.config['MYSQL_DATABASE_HOST'] = config('MYSQL_HOST')
    app.config['MYSQL_DATABASE_USER'] = config('MYSQL_USER')
    app.config['MYSQL_DATABASE_PASSWORD'] = config('MYSQL_PASSWORD')
    app.config['MYSQL_DATABASE_DB'] = config('MYSQL_DB')
    mysql.init_app(app)

def get_connection():

    return mysql.connect()