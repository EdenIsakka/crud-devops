
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Doctor, Enfermera, Paciente
from schemas import DoctorCreate, DoctorUpdate, DoctorOut, EnfermeraCreate, EnfermeraUpdate, EnfermeraOut, PacienteCreate, PacienteUpdate, PacienteOut

# Crear las tablas
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {'message': 'API funcionando correctamente'}

# Dependencia para obtener la sesión de la BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/doctors/", response_model=DoctorOut)
def create_doctor(doctor: DoctorCreate, db: Session = Depends(get_db)):
    db_doctor = Doctor(**doctor.dict())
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor


@app.get("/doctors/", response_model=list[DoctorOut])
def read_doctors(db: Session = Depends(get_db)):
    doctors = db.query(Doctor).all()
    return doctors


@app.get("/doctors/{doctor_id}", response_model=DoctorOut)
def read_doctor(doctor_id: int, db: Session = Depends(get_db)):
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor no encontrado")
    return doctor


@app.put("/doctors/{doctor_id}", response_model=DoctorOut)
def update_doctor(doctor_id: int, doctor_update: DoctorCreate, db: Session = Depends(get_db)):
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor no encontrado")
    doctor.nombre = doctor_update.nombre
    doctor.apellido = doctor_update.apellido
    doctor.correo = doctor_update.correo
    db.commit()
    db.refresh(doctor)
    return doctor


@app.patch("/doctors/{doctor_id}", response_model=DoctorOut)
def patch_doctor(doctor_id: int, doctor_update: DoctorUpdate, db: Session = Depends(get_db)):
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor no encontrado")
    update_data = doctor_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(doctor, key, value)
    db.commit()
    db.refresh(doctor)
    return doctor

@app.delete("/doctors/{doctor_id}")
def delete_doctor(doctor_id: int, db: Session = Depends(get_db)):
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor no encontrado")
    db.delete(doctor)
    db.commit()
    return {"mensaje": "Doctor eliminado correctamente"}



@app.post("/enfermeras/", response_model=EnfermeraOut)
def create_enfermera(enfermera: EnfermeraCreate, db: Session = Depends(get_db)):
    db_enfermera = Enfermera(**enfermera.dict())
    db.add(db_enfermera)
    db.commit()
    db.refresh(db_enfermera)
    return db_enfermera

@app.get("/enfermeras/", response_model=list[EnfermeraOut])
def read_enfermeras(db: Session = Depends(get_db)):
    enfermeras = db.query(Enfermera).all()
    return enfermeras

@app.get("/enfermeras/{enfermera_id}", response_model=EnfermeraOut)
def read_enfermera(enfermera_id: int, db: Session = Depends(get_db)):
    enfermera = db.query(Enfermera).filter(Enfermera.id == enfermera_id).first()
    if not enfermera:
        raise HTTPException(status_code=404, detail="Enfermera no encontrada")
    return enfermera

@app.put("/enfermeras/{enfermera_id}", response_model=EnfermeraOut)
def update_enfermera(enfermera_id: int, enfermera_update: EnfermeraCreate, db: Session = Depends(get_db)):
    enfermera = db.query(Enfermera).filter(Enfermera.id == enfermera_id).first()
    if not enfermera:
        raise HTTPException(status_code=404, detail="Enfermera no encontrada")
    enfermera.nombre = enfermera_update.nombre
    enfermera.apellido = enfermera_update.apellido
    enfermera.correo = enfermera_update.correo
    db.commit()
    db.refresh(enfermera)
    return enfermera

@app.patch("/enfermeras/{enfermera_id}", response_model=EnfermeraOut)
def patch_enfermera(enfermera_id: int, enfermera_update: EnfermeraUpdate, db: Session = Depends(get_db)):
    enfermera = db.query(Enfermera).filter(Enfermera.id == enfermera_id).first()
    if not enfermera:
        raise HTTPException(status_code=404, detail="Enfermera no encontrada")
    update_data = enfermera_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(enfermera, key, value)
    db.commit()
    db.refresh(enfermera)
    return enfermera

@app.delete("/enfermeras/{enfermera_id}")
def delete_enfermera(enfermera_id: int, db: Session = Depends(get_db)):
    enfermera = db.query(Enfermera).filter(Enfermera.id == enfermera_id).first()
    if not enfermera:
        raise HTTPException(status_code=404, detail="Enfermera no encontrada")
    db.delete(enfermera)
    db.commit()
    return {"mensaje": "Enfermera eliminada correctamente"}


@app.post("/pacientes/", response_model=PacienteOut)
def create_paciente(paciente: PacienteCreate, db: Session = Depends(get_db)):
    db_paciente = Paciente(**paciente.dict())
    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente

@app.get("/pacientes/", response_model=list[PacienteOut])
def read_pacientes(db: Session = Depends(get_db)):
    pacientes = db.query(Paciente).all()
    return pacientes

@app.get("/pacientes/{paciente_id}", response_model=PacienteOut)
def read_paciente(paciente_id: int, db: Session = Depends(get_db)):
    paciente = db.query(Paciente).filter(Paciente.id == paciente_id).first()
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return paciente

@app.put("/pacientes/{paciente_id}", response_model=PacienteOut)
def update_paciente(paciente_id: int, paciente_update: PacienteCreate, db: Session = Depends(get_db)):
    paciente = db.query(Paciente).filter(Paciente.id == paciente_id).first()
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    paciente.nombre = paciente_update.nombre
    paciente.apellido = paciente_update.apellido
    paciente.correo = paciente_update.correo
    db.commit()
    db.refresh(paciente)
    return paciente

@app.patch("/pacientes/{paciente_id}", response_model=PacienteOut)
def patch_paciente(paciente_id: int, paciente_update: PacienteUpdate, db: Session = Depends(get_db)):
    paciente = db.query(Paciente).filter(Paciente.id == paciente_id).first()
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    update_data = paciente_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(paciente, key, value)
    db.commit()
    db.refresh(paciente)
    return paciente

@app.delete("/pacientes/{paciente_id}")
def delete_paciente(paciente_id: int, db: Session = Depends(get_db)):
    paciente = db.query(Paciente).filter(Paciente.id == paciente_id).first()
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    db.delete(paciente)
    db.commit()
    return {"mensaje": "Paciente eliminado correctamente"}
