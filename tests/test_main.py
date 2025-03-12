# tests/test_main.py
from fastapi.testclient import TestClient
from main import app  # Asegúrate de que 'app' es el objeto FastAPI exportado en main.py

client = TestClient(app)

def test_get_empty_doctors():
    response = client.get("/doctors/")
    assert response.status_code == 200
    # Suponiendo que la base de datos de pruebas esté vacía
    assert response.json() == []

def test_create_doctor():
    doctor_data = {
        "nombre": "Juan",
        "apellido": "Perez",
        "correo": "juanperez@example.com"
    }
    response = client.post("/doctors/", json=doctor_data)
    assert response.status_code == 200  # O 201, según cómo configures tu respuesta
    data = response.json()
    assert data["nombre"] == doctor_data["nombre"]
    assert data["apellido"] == doctor_data["apellido"]
    assert data["correo"] == doctor_data["correo"]
    assert "id" in data  # El ID se genera automáticamente

def test_get_doctor_by_id():
    doctor_data = {
        "nombre": "Ana",
        "apellido": "Garcia",
        "correo": "anagarcia@example.com"
    }
    response = client.post("/doctors/", json=doctor_data)
    doctor_id = response.json()["id"]

    response_get = client.get(f"/doctors/{doctor_id}")
    assert response_get.status_code == 200
    data = response_get.json()
    assert data["id"] == doctor_id
    assert data["nombre"] == doctor_data["nombre"]

def test_update_doctor():
    # Crear doctor
    doctor_data = {
        "nombre": "Carlos",
        "apellido": "Lopez",
        "correo": "carloslopez@example.com"
    }
    response = client.post("/doctors/", json=doctor_data)
    doctor_id = response.json()["id"]

    # Datos actualizados (PUT requiere enviar todos los campos)
    updated_data = {
        "nombre": "Carlos Actualizado",
        "apellido": "Lopez Actualizado",
        "correo": "carlosactualizado@example.com"
    }
    response_put = client.put(f"/doctors/{doctor_id}", json=updated_data)
    assert response_put.status_code == 200
    data = response_put.json()
    assert data["nombre"] == updated_data["nombre"]
    assert data["apellido"] == updated_data["apellido"]
    assert data["correo"] == updated_data["correo"]

def test_patch_doctor():
    # Crear doctor
    doctor_data = {
        "nombre": "Laura",
        "apellido": "Martinez",
        "correo": "lauramartinez@example.com"
    }
    response = client.post("/doctors/", json=doctor_data)
    doctor_id = response.json()["id"]

    # Actualización parcial: solo el nombre
    patch_data = {"nombre": "Laura Actualizada"}
    response_patch = client.patch(f"/doctors/{doctor_id}", json=patch_data)
    assert response_patch.status_code == 200
    data = response_patch.json()
    assert data["nombre"] == "Laura Actualizada"
    # Se verifica que los otros campos permanecen iguales
    assert data["apellido"] == doctor_data["apellido"]

def test_delete_doctor():
    # Crear doctor
    doctor_data = {
        "nombre": "Miguel",
        "apellido": "Sanchez",
        "correo": "miguelsanchez@example.com"
    }
    response = client.post("/doctors/", json=doctor_data)
    doctor_id = response.json()["id"]

    # Eliminar el doctor
    response_delete = client.delete(f"/doctors/{doctor_id}")
    assert response_delete.status_code == 200

    # Intentar obtenerlo debería dar un error (por ejemplo, 404)
    response_get = client.get(f"/doctors/{doctor_id}")
    assert response_get.status_code == 404

def test_get_nonexistent_doctor():
    response = client.get("/doctors/9999")  # Suponiendo que no existe el ID 9999
    assert response.status_code == 404


def test_update_nonexistent_doctor():
    updated_data = {
        "nombre": "NuevoNombre",
        "apellido": "NuevoApellido",
        "correo": "nuevo@example.com"
    }
    response = client.put("/doctors/9999", json=updated_data)
    assert response.status_code == 404


def test_patch_nonexistent_doctor():
    patch_data = {"nombre": "NombreActualizado"}
    response = client.patch("/doctors/9999", json=patch_data)
    assert response.status_code == 404

def test_create_and_get_enfermera():
    enfermera_data = {
        "nombre": "Ana",
        "apellido": "Gomez",
        "correo": "ana.gomez@example.com"
    }
    # Crear enfermera
    create_response = client.post("/enfermeras/", json=enfermera_data)
    assert create_response.status_code == 200
    enfermera_id = create_response.json()["id"]

    # Obtener enfermera
    get_response = client.get(f"/enfermeras/{enfermera_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["nombre"] == enfermera_data["nombre"]

def test_update_enfermera():
    # Crear enfermera
    enfermera_data = {
        "nombre": "Ana",
        "apellido": "Gomez",
        "correo": "ana.gomez@example.com"
    }
    create_response = client.post("/enfermeras/", json=enfermera_data)
    assert create_response.status_code == 200
    enfermera_id = create_response.json()["id"]

    # Actualizar la enfermera (PUT)
    updated_data = {
        "nombre": "Ana Actualizada",
        "apellido": "Gomez Actualizado",
        "correo": "ana.actualizada@example.com"
    }
    update_response = client.put(f"/enfermeras/{enfermera_id}", json=updated_data)
    assert update_response.status_code == 200
    data = update_response.json()
    assert data["nombre"] == updated_data["nombre"]
    assert data["apellido"] == updated_data["apellido"]
    assert data["correo"] == updated_data["correo"]

def test_patch_enfermera():
    # Crear enfermera
    enfermera_data = {
        "nombre": "Sofia",
        "apellido": "Lopez",
        "correo": "sofia.lopez@example.com"
    }
    create_response = client.post("/enfermeras/", json=enfermera_data)
    assert create_response.status_code == 200
    enfermera_id = create_response.json()["id"]

    # Actualización parcial (PATCH): cambiar solo el nombre
    patch_data = {"nombre": "Sofia Patch"}
    patch_response = client.patch(f"/enfermeras/{enfermera_id}", json=patch_data)
    assert patch_response.status_code == 200
    data = patch_response.json()
    assert data["nombre"] == "Sofia Patch"
    # Verifica que otros campos se mantienen sin cambios
    assert data["apellido"] == enfermera_data["apellido"]
    assert data["correo"] == enfermera_data["correo"]

def test_delete_enfermera():
    # Crear enfermera
    enfermera_data = {
        "nombre": "Maria",
        "apellido": "Rodriguez",
        "correo": "maria.rodriguez@example.com"
    }
    create_response = client.post("/enfermeras/", json=enfermera_data)
    assert create_response.status_code == 200
    enfermera_id = create_response.json()["id"]

    # Eliminar la enfermera
    delete_response = client.delete(f"/enfermeras/{enfermera_id}")
    assert delete_response.status_code == 200

    # Verificar que ya no se puede obtener la enfermera (debe retornar 404)
    get_response = client.get(f"/enfermeras/{enfermera_id}")
    assert get_response.status_code == 404

def test_update_paciente():
    # Crear paciente
    paciente_data = {
        "nombre": "Juan",
        "apellido": "Perez",
        "correo": "juan.perez@example.com"
    }
    create_response = client.post("/pacientes/", json=paciente_data)
    assert create_response.status_code == 200
    paciente_id = create_response.json()["id"]

    # Actualizar paciente (PUT)
    updated_data = {
        "nombre": "Juan Actualizado",
        "apellido": "Perez Actualizado",
        "correo": "juan.actualizado@example.com"
    }
    update_response = client.put(f"/pacientes/{paciente_id}", json=updated_data)
    assert update_response.status_code == 200
    data = update_response.json()
    assert data["nombre"] == updated_data["nombre"]
    assert data["apellido"] == updated_data["apellido"]
    assert data["correo"] == updated_data["correo"]

def test_patch_paciente():
    # Crear paciente
    paciente_data = {
        "nombre": "Luis",
        "apellido": "Garcia",
        "correo": "luis.garcia@example.com"
    }
    create_response = client.post("/pacientes/", json=paciente_data)
    assert create_response.status_code == 200
    paciente_id = create_response.json()["id"]

    # Actualización parcial (PATCH): cambiar solo el apellido
    patch_data = {"apellido": "Garcia Patch"}
    patch_response = client.patch(f"/pacientes/{paciente_id}", json=patch_data)
    assert patch_response.status_code == 200
    data = patch_response.json()
    assert data["apellido"] == "Garcia Patch"
    # Verifica que otros campos se mantienen sin cambios
    assert data["nombre"] == paciente_data["nombre"]
    assert data["correo"] == paciente_data["correo"]

def test_delete_paciente():
    # Crear paciente
    paciente_data = {
        "nombre": "Carlos",
        "apellido": "Fernandez",
        "correo": "carlos.fernandez@example.com"
    }
    create_response = client.post("/pacientes/", json=paciente_data)
    assert create_response.status_code == 200
    paciente_id = create_response.json()["id"]

    # Eliminar el paciente
    delete_response = client.delete(f"/pacientes/{paciente_id}")
    assert delete_response.status_code == 200

    # Verificar que ya no se puede obtener el paciente (retorna 404)
    get_response = client.get(f"/pacientes/{paciente_id}")
    assert get_response.status_code == 404
