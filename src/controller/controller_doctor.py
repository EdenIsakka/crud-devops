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

def read_medicos():
    try:
        print("📡 Iniciando la obtención de médicos")  # Depuración
        medicos = ServiceDoctor.read_doctor()

        if not medicos:
            print("⚠️ No se encontraron médicos en la base de datos.")  # Debug
            return jsonify({"error": False, "message": "No hay médicos registrados", "data": []}), 200

        print(f"📡 Médicos obtenidos: {medicos}")  # Debug
        return jsonify({"error": False, "message": "Datos obtenidos", "data": medicos}), 200
    except Exception as e:
        print(f"❌ ERROR en read_medicos: {repr(e)}")  # 🔥 Ahora mostrará el error real
        return jsonify({"error": True, "message": f"Ocurrió un error: {repr(e)}"}), 500
    
def update_doctor(id):
    try:
        data = request.get_json
        doctor = DoctorSchema(**data())
        response = ServiceDoctor.update_doctor(id,doctor)
        return jsonify(response),201
    except ValidationError as e:
        return jsonify({'error': True, 'message': 'Datos invalidos', 'details': e.errors()}),400
    except Exception as e:
        return jsonify({'error': True, 'message': f'error inesperado: {e}'}), 500
    
def patch_doctor(id):
    try:
        data = request.get_json
        doctor = DoctorSchema(**data())
        response = ServiceDoctor.patch_doctor(id,doctor)
        return jsonify(response),201
    except ValidationError as e:
        return jsonify({'error': True, 'message':'Datos invalidos', 'details': e.errors()},400)
    except Exception as e:
        return jsonify({'error': True, 'message': f'error inesperado: {e}' }),500


def delete_doctor(id):
    try:
        response = ServiceDoctor.delete_doctor(id)
        return jsonify(response), 204
    except Exception as e:
        return jsonify({'error': True, 'message': f'Error inesperado: {e}'}), 500
    