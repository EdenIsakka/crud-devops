from flask import Flask
from flask import render_template, request, jsonify
from repository.db_mysql import get_connection


class ServiceDoctor:

    @classmethod
    def save_doctor(cls,doctor):
        try:
            query = "INSERT INTO `medicos` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL,%s,%s,%s);"
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
            return {
                'error': True,
                'message': f'Ocurrio un error : {e}'
            }
