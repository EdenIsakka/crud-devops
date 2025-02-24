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


@app.route('/create-medicos', methods=['POST'])
def save():
    try:
        data = request.get_json()
        
        _nombre = data["txtNombre"]
        _correo= data["txtCorreo"]
        _foto = data["txtFoto"]
        
        query = "INSERT INTO `medicos` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL,%s,%s,%s);"

        datos=(_nombre,_correo,_foto)

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(query,datos)
        conn.commit()
        cursor.close()

        response = {
            'error' : False,
            'message': 'Data creada con exito',
            'data' : data
        }
        return jsonify(response), 201
    except Exception as e:
        response = {
            'error' : True,
            'message': f'Ocurrio un Error: {e}',
            'data' : None
        }

        return jsonify(response), 500


@app.route("/read-medicos", methods =['GET'])
def read():
    try:

        conn = mysql.connect()
        cursor = conn.cursor()

        query = 'SELECT * FROM medicos'

        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()

        items = [{'txtNombre': item[1], 'txtCorreo': item[2], 'txtFoto': item[0]} for item in data]
    
        response = {
        'error':False,
        'message': "Item obtenido con exito",
        'data' : items
    }


        return jsonify(response), 200
    except Exception as e:
     response = {
        'error':True,
        'message': f"Error Obteniendo el Item: {e}",
        'data' : None,
    }

    return jsonify(response), 500




if __name__ == '__main__':
    app.run(debug=True)
