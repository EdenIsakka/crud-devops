from http.client import HTTPException

from fastapi import FastAPI
from schemas import DoctorCreate, EnfermeraCreate, PacienteCreate
import httpx
import json

app = FastAPI()

@app.post("/doctors/")
def create_doctor(doctor: DoctorCreate):
    ...

@app.post("/enfermeras/")
def create_enfermera(enfermera: EnfermeraCreate):
    ...

@app.post("/pacientes/")
def create_paciente(paciente: PacienteCreate):
    ...
@app.post("/publish/")
async def publish_message():
    try:
        message_string = json.dumps({
            "type": "event",
            "sendTo": "microservice2"
        })

        url = "https://house-inventory-devops-production.up.railway.app/api/v2/messages/publish"
        headers = {
            "Content-Type": "application/json",
            "X-Source": "coordinator",
            "X-Destination": "queue-ms"
        }

        payload = {
            "message": message_string
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, json=payload)

        return {
            "status": "Mensaje publicado",
            "enviado": payload,
            "respuesta_microservicio": response.text
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al publicar el mensaje: {e}")


