# publisher.py
import os
from fastapi import APIRouter, HTTPException
import httpx
import json
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

POST_URL = os.getenv("POST_URL")


@router.post("/publish/")
async def publish_message():
    try:
        message_string = json.dumps({
            "type": "event",
            "sendTo": "microservice1"
        })

        headers = {
            "Content-Type": "application/json",
            "X-Source": "coordinator",
            "X-Destination": "queue-ms"
        }

        payload = {
            "message": message_string
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(POST_URL, headers=headers, json=payload)

        return {
            "status": "Mensaje publicado",
            "enviado": payload,
            "respuesta_microservicio": response.text
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al publicar el mensaje: {e}")
