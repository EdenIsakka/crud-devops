from flask import request, jsonify
from pydantic import ValidationError
from services.doctor_services import ServiceDoctor
from utils.schemas import DoctorSchema

def create_doctor(): #Endpoint Create
    try:
        data = request.get_json
        doctor = DoctorSchema(**data()) #Validacion con Pydantic
        response = ServiceDoctor.create_doctor(doctor)
        return jsonify(response), 201
    except ValidationError as e:
        return jsonify({'error': True, 'message':'Datos Invalidos', 'details':e.errors()}), 400
    except Exception as e:
        return jsonify({'error': True, 'message': f"Error inesperado: {e}"}), 500

def read_doctor():
    try:
        response = ServiceDoctor.read_doctor()
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': True, 'message': f'Error inesperado: {e}'}), 500
    
def update_doctor(id):
    try:
        data = request.get_json()
        doctor = DoctorSchema(**data())
        response = ServiceDoctor.update_doctor(id,doctor)
        return jsonify(response),201
    except ValidationError as e:
        return jsonify({'error': True, 'message': 'Datos invalidos', 'details': e.errors()}),400
    except Exception as e:
        return jsonify({'error': True, 'message': f'error inesperado: {e}'}), 500