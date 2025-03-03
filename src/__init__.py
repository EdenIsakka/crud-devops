from flask import Flask
from controller.controller_doctor import create_doctor, read_doctor, update_doctor, patch_doctor, delete_doctor
from repository.db_mysql import init_db

app = Flask(__name__)
init_db(app) #Config la base de datos

app.add_url_rule('/create-doctor','create_doctor', create_doctor, methods=['POST'])
app.add_url_rule('/read-medicos', 'read_doctor', read_doctor, methods=['GET'])
app.add_url_rule('/update-medicos/<int:id>', 'update_doctor', update_doctor, methods =['PUT'])
app.add_url_rule('/patch-medicos/<int:id>','patch_doctor', patch_doctor, methods =['PATCH'])
app.add_url_rule('/delete-medicos/<int:id>', 'delete_doctor', delete_doctor, methods =['DELETE'])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
