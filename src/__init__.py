from flask import Flask
from controller.controller_doctor import create_doctor


app = Flask(__name__)

app.add_url_rule('/doctores', 'create_doctor',create_doctor, methods=['POST'])


if __name__ == '__main__':
    app.run(debug=True)