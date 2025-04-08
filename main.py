from fastapi import FastAPI
from schemas import DoctorCreate, EnfermeraCreate, PacienteCreate
from services.queue_sender import enviar_mensaje_a_cola

app = FastAPI()

@app.post("/doctors/")
def create_doctor(doctor: DoctorCreate):
    data = {
        "action": "create",
        "model": "doctor",
        "payload": doctor.dict()
    }
    enviar_mensaje_a_cola(data)
    return {"status": "mensaje enviado a la cola"}

@app.post("/enfermeras/")
def create_enfermera(enfermera: EnfermeraCreate):
    data = {
        "action": "create",
        "model": "enfermera",
        "payload": enfermera.dict()
    }
    enviar_mensaje_a_cola(data)
    return {"status": "mensaje enviado a la cola"}

@app.post("/pacientes/")
def create_paciente(paciente: PacienteCreate):
    data = {
        "action": "create",
        "model": "paciente",
        "payload": paciente.dict()
    }
    enviar_mensaje_a_cola(data)
    return {"status": "mensaje enviado a la cola"}
