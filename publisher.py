# publisher.py

from fastapi import APIRouter, HTTPException
import httpx
import json

router = APIRouter()

@router.post("/publish/")
async def publish_message():
    try:
        message_string = json.dumps({
            "type": "event",
            "sendTo": "microservice1"
        })

        url = "http://localhost:8080/api/v2/messages"
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
