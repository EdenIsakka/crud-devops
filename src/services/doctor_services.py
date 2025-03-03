from flask import Flask
from flask import render_template, request, jsonify
from repository.db_mysql import get_connection
from utils.schemas import DoctorSchema


class ServiceDoctor:

    @classmethod
    def create_doctor(cls,doctor):
        try:
            query = "INSERT INTO `medicos` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, %s,%s,%s);"
            datos = (doctor.nombre, doctor.correo, doctor.foto)

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

            query = "UPDATE medicos SET nombre = %s, correo = %s, foto =%s WHERE id = %s"
            datos = (doctor_data.nombre, doctor_data.correo, doctor_data.foto, doc_id )

            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(query,datos)
            conn.commit()
            cursor.close()

            return {'error': False, 'message': f'Doctor con ID {doc_id} actualizado correctamente'}
        except Exception as e:
            return {'error': True, 'message': f'Error actualizando el doctor: {e}'}

    @classmethod
    def patch_doctor(cls, doc_id, updates):
        try:
            if isinstance (updates, DoctorSchema):
                updates = updates.model_dump()

            update_fields = ", ".join(f"{key} = %s" for key in updates.keys())
            query = f"UPDATE medicos SET {update_fields} WHERE id = %s"
            values = list(updates.values()) + [doc_id]

            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(query,values)
            conn.commit()
            cursor.close()

            return {'error': False, 'message': f'Doctor con ID {doc_id} actualizado correctamente'}
        except Exception as e:
            return {'error': True, 'message': f'Error actualizando el doctor: {e}'}

    @classmethod
    def delete_doctor(cls,doc_id):
        try:
            query = "DELETE FROM medicos WHERE id = %s;"
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(query, (doc_id,))
            conn.commit()

            if cursor.rowcount == 0: #Verifica si realmente se elimina el doc
                return {'error': True, 'message': f'No se Encontro un doctor con ID {doc_id}'}
            
            cursor.close()
            return {'error': False, 'message': f'Doctor con ID {doc_id} eliminado correctamente'}
        except Exception as e:
            return {'error':True, 'message': f'error eliminando el doctor: {e}'}
             

        
          
            
