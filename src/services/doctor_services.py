from flask import Flask
from flask import render_template, request, jsonify
from repository.db_mysql import get_connection
from utils.schemas import DoctorSchema


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
          doctors = cursor.fetchall() or []
          cursor.close()

          doctors_list = [{'id': doc[0], 'nombre': doc[1], 'correo': doc[2], 'foto': doc[3]} for doc in doctors]

          return {'error': False, 'message': 'Lista de medicos obtenida con exito', 'data':doctors_list}
      except Exception as e:
          return {'error': True, 'message': f'Ocurrio un error: {e}'}
      
    @classmethod
    def update_doctor(cls, doc_id, doctor_data):
        try:
            if isinstance(doctor_data, dict): #Verifica si doctor_data es un dic y lo convierte a obj Pydantic
                doctor_data = DoctorSchema(**doctor_data()) #Convierte en obj valido

            query = "UPDATE medicos SET nombre = %s, correo = %s, foto =%s WHERE id = %s"
            datos = (doctor_data.txtNombre, doctor_data.txtCorreo, doctor_data.txtFoto, doc_id )

            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(query,datos)
            conn.commit()
            cursor.close()

            return {'error': False, 'message': f'Doctor con ID {doc_id} actualizado correctamente'}
        except Exception as e:
            return {'error': True, 'message': f'Error actualizando el doctor: {e}'}



          
            
