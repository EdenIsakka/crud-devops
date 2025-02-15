from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL


app = Flask(__name__) #Creado de la app 

mysql = MySQL()
app.config['MYSQL_DATABSE_HOST']='localhost' #Configuracion para que se conecte a la DB utilice el hostlocal
app.config['MYSQL_DATABSE_USER']='root'
app.config['MYSQL_DATABSE_PASSWORD']=''
app.config['MYSQL_DATABSE_DB']='sistema'
mysql.init_app(app)


@app.route("/") #Ruteo de la app 
def index():

    sql = "INSERT INTO `medicos` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, 'Santiago', 'santiago333@hotmail.com', 'foto.jpg');"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

    return render_template('medicos/index.html') 

if __name__ == '__main__':
    app.run(debug=True)
