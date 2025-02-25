from flask import Flask
from flask import render_template, request, jsonify
from flaskext.mysql import MySQL

mysql = MySQL()

class ServiceDoctor():
    @classmethod
    def save_doctor():
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