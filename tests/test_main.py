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
