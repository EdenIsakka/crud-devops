import os
import uuid
import httpx
import json
from fastapi import APIRouter, Request, HTTPException
from azure.storage.queue import QueueClient
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()
QUEUE_NAME = "processed-1-3"
AZURE_QUEUE_CONNECTION_STRING = os.getenv("AZURE_QUEUE_CONNECTION_STRING")


@router.post("/consume-saga/")
async def consume_saga():
    try:
        queue_client = QueueClient.from_connection_string(
            conn_str=AZURE_QUEUE_CONNECTION_STRING,
            queue_name=QUEUE_NAME
        )

        messages = queue_client.receive_messages(messages_per_page=1)

        for msg in messages:
            content = msg.content  # este es string, ya viene serializado
            print(f"[SAGA EVENTO RECIBIDO] {content}")

            # Enviar al microservicio vía HTTP
            url = "http://localhost:8080/api/v2/messages"
            headers = {
                "Content-Type": "application/json",
                "X-Source": "coordinator",
                "X-Destination": "queue-ms"
            }
            data = {
                "message": content  # ya es string JSON
            }

            async with httpx.AsyncClient() as client:
                response = await client.post(url, headers=headers, json=data)

            # Eliminar el mensaje de la cola
            queue_client.delete_message(msg)

            return {
                "status": "Mensaje reenviado",
                "data_enviado": data,
                "respuesta_ms": response.text
            }

        return {"status": "No hay mensajes en la cola"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al consumir o reenviar: {e}")