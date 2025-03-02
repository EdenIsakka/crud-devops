from flask import Flask
from flask import render_template, request, jsonify
from repository.db_mysql import get_connection


class ServiceDoctor:

    @classmethod
    def create_doctor(cls,doctor):
        try:
            query = "INSERT INTO `medicos` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, %s,%s,%s);"
            datos = (doctor.txtNombre, doctor.txtCorreo, doctor.txtFoto)

            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(query,datos)
            conn.commit()
            cursor.close()

            return {
                'error' : False,
                'message': 'Medico creado con exito',
                'data': doctor.dict()
            }
        except Exception as e:
            return {'error': True, 'message': f'Ocurrio un error: {e}'}
        
    @classmethod
    def read_doctor(cls):
      try:
          query = 'SELECT * FROM medicos;'
          conn = get_connection()
          cursor = conn.cursor()
          cursor.execute(query)
          doctors = cursor.fetchall()
          cursor.close()

          doctors_list = [{'id': doc[0], 'nombre': doc[1], 'correo': doc[2], 'foto': doc[3]} for doc in doctors]

          return {'error': False, 'message': 'Lista de medicos obtenida con exito', 'data':doctors_list}
      except Exception as e:
          return {'error': True, 'message': f'Ocurrio un error: {e}'}
          
            
