from flask import request, jsonify
from pydantic import ValidationError
from services.doctor_services import ServiceDoctor
from utils.schemas import DoctorSchema

def create_doctor(): #Endpoint Create
    try:
        data = request.get_json
        doctor = DoctorSchema(**data()) #Validacion con Pydantic
        response = ServiceDoctor.save_doctor(doctor)
        return jsonify(response), 201
    except ValidationError as e:
        return jsonify({'error': True, 'message':'Datos Invalidos', 'details':e.errors()}), 400
    except Exception as e:
        return jsonify({'error': True, 'message': f"Error inesperado: {e}"}), 500
