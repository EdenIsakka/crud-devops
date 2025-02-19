from flask import Flask
from flask import render_template, request, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__) #Creado de la app 

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'sistema'
mysql.init_app(app)


@app.route("/") #Ruteo de la app 
def index():

    
    return render_template('medicos/index.html') 

@app.route('/create')
def create():

    return render_template('medicos/create.html')

@app.route('/store', methods=['POST'])
def storage():
    data = request.get_json()
    
    _nombre = data["txtNombre"]
    _correo= data["txtCorreo"]
    _foto = data["txtFoto"]
    
    sql = "INSERT INTO `medicos` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL,%s,%s,%s);"

    datos=(_nombre,_correo,_foto)

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()

    response = {
        "txtNombre": _nombre,
        "txtCorreo": _correo,
        "txtFoto": _foto
    }
    return jsonify(response), 201
if __name__ == '__main__':
    app.run(debug=True)
