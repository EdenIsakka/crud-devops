from flask import Flask
from flask import render_template, request
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

    sql = "INSERT INTO `medicos` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, 'Santiago', 'santiago333@hotmail.com', 'foto.jpg');"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

    return render_template('medicos/index.html') 

@app.route('/create')
def create():

    return render_template('medicos/create.html')

@app.route('/store', methods=['POST'])
def storage():
    _nombre = request.form['txtNombre']
    _correo= request.form['txtCorreo']

    _foto = request.files['txtFoto']

    
    sql = "INSERT INTO `medicos` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL,%s,%s,%s);"

    datos=(_nombre,_correo,_foto.filename)

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()

if __name__ == '__main__':
    app.run(debug=True)
