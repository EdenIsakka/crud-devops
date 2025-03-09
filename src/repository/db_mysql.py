import os
import pymysql
from flask_mysqldb import MySQL 
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
        conn = pymysql.connect(
            host=os.getenv("MYSQL_HOST", "mysql"),
            port=int(os.getenv("MYSQL_PORT", 3306)),
            user=os.getenv("MYSQL_USER", "admin"),
            password=os.getenv("MYSQL_PASSWORD", "admin"),
            db=os.getenv("MYSQL_DB", "sistema"),
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Conexión a MySQL exitosa")
        return conn
    except Exception as e:
        print(f"ERROR en la conexión a MySQL: {e}")
        return None