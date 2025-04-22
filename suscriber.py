# subscriber.py

import os
import json
from azure.servicebus import ServiceBusClient, ServiceBusMessage
from dotenv import load_dotenv

load_dotenv()

# Conexión

CONNECTION_STR = os.getenv("CONNECTION_STR")
TOPIC_NAME = os.getenv("TOPIC_NAME")
SUBSCRIPTION_NAME = os.getenv("SUBSCRIPTION_NAME")

def generate_fake_data():
    return {
        "doctor": {"nombre": "Carlos", "apellido": "González", "correo": "carlos@example.com"},
        "enfermera": {"nombre": "Lucía", "apellido": "Ramírez", "correo": "lucia@example.com"},
        "paciente": {"nombre": "Juan", "apellido": "Martínez", "correo": "juan@example.com"}
    }

def process_message(message):
    try:
        # Leer y decodificar el mensaje
        raw_body = str(message)
        body = json.loads(raw_body)

        # Enriquecer con datos del microservicio
        enriched = {**body, **generate_fake_data()}

        # Mostrar resultado
        print("\n📥 MENSAJE RECIBIDO Y PROCESADO:")
        print(json.dumps(enriched, indent=2))

    except Exception as e:
        print(f"❌ Error al procesar mensaje: {e}")

def main():
    print("🔊 Escuchando la subscripción 'coordinator' en topic 'manage-messages'...")

    with ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR) as client:
        receiver = client.get_subscription_receiver(
            topic_name=TOPIC_NAME,
            subscription_name=SUBSCRIPTION_NAME
        )

        with receiver:
            for msg in receiver:
                process_message(str(msg))
                receiver.complete_message(msg)

if __name__ == "__main__":
    main()