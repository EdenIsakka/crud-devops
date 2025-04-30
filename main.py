from fastapi import FastAPI, HTTPException, Request
import httpx
import json
from schemas import DoctorCreate, EnfermeraCreate, PacienteCreate
import os
from dotenv import load_dotenv

load_dotenv()

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
async def publish_message(request: Request):
    try:
        # Leer el cuerpo del Postman
        body = await request.json()
        send_to = body.get("sendTo")

        if not send_to:
            raise HTTPException(status_code=400, detail="El campo 'sendTo' es obligatorio")

        # Construir el mensaje a enviar
        message_string = json.dumps({
            "type": "event",
            "sendTo": send_to
        })

        url = os.getenv("POST_URL", "https://house-inventory-devops-production.up.railway.app/api/v2/messages/publish")
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
