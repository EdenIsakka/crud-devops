from flask import Flask
from controller.controller_doctor import create_doctor, read_doctor, update_doctor
from repository.db_mysql import init_db

app = Flask(__name__)
init_db(app) #Config la base de datos

app.add_url_rule('/create-doctor','create_doctor', create_doctor, methods=['POST'])
app.add_url_rule('/read-medicos', 'read_doctor', read_doctor, methods=['GET'])
app.add_url_rule('/update-medicos/<int:id>', 'update_doctor', update_doctor, methods =['PUT'])

if __name__ == '__main__':
    app.run(debug=True)