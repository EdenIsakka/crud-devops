from flask import Flask
from flaskext.mysql import MySQL


#Controllers

from .controller import controller_doctor

app = Flask(__name__)
mysql = MySQL()


def init_app(config):
    #Configuracion
    app.config.from_object(config)