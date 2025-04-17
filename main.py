from fastapi import FastAPI
from schemas import DoctorCreate, EnfermeraCreate, PacienteCreate
from services import publisher

app = FastAPI()

@app.post("/doctors/")
def create_doctor(doctor: DoctorCreate):
    data = {
        "action": "create",
        "model": "doctor",
        "payload": doctor.dict()
    }

@app.post("/enfermeras/")
def create_enfermera(enfermera: EnfermeraCreate):
    data = {
        "action": "create",
        "model": "enfermera",
        "payload": enfermera.dict()
    }


@app.post("/pacientes/")
def create_paciente(paciente: PacienteCreate):
    data = {
        "action": "create",
        "model": "paciente",
        "payload": paciente.dict()
    }

app.include_router(publisher.router, prefix="/saga")