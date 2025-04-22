from fastapi import APIRouter, HTTPException, Request
from azure.servicebus import ServiceBusClient, ServiceBusMessage
from dotenv import load_dotenv
import os
import json

load_dotenv()

router = APIRouter()

CONNECTION_STR = os.getenv("CONNECTION_STR")
TOPIC_NAME = os.getenv("TOPIC_NAME")

@router.post("/publish/")
async def publish_to_topic(request: Request):
    try:
        # 1. Recibir JSON desde Postman
        data = await request.json()

        # 2. Validar campo requerido
        send_to = data.get("sendTo")
        if not send_to:
            raise HTTPException(status_code=400, detail="El campo 'sendTo' es obligatorio")

        # 3. Construir cuerpo del mensaje que se va a publicar
        message_dict = {
            "type": "event",
            "sendTo": send_to
        }
        message_str = json.dumps(message_dict)

        # 4. Publicar en Azure Topic
        with ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR) as client:
            sender = client.get_topic_sender(topic_name=TOPIC_NAME)
            with sender:
                message = ServiceBusMessage(message_str)
                message.application_properties = {
                    "source": "coordinator",
                    "destination": send_to
                }
                sender.send_messages(message)

        return {
            "status": "Mensaje enviado correctamente",
            "publicado": message_dict
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al enviar mensaje: {e}")
