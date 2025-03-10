# schemas.py
from pydantic import BaseModel

# Esquemas para Doctor
class DoctorBase(BaseModel):
    nombre: str
    apellido: str
    correo: str

class DoctorCreate(DoctorBase):
    pass

class DoctorUpdate(BaseModel):
    nombre: str | None = None
    apellido: str | None = None
    correo: str | None = None

class DoctorOut(DoctorBase):
    id: int

    class Config:
        orm_mode = True

# Repite lo mismo para Enfermera
class EnfermeraBase(BaseModel):
    nombre: str
    apellido: str
    correo: str

class EnfermeraCreate(EnfermeraBase):
    pass

class EnfermeraUpdate(BaseModel):
    nombre: str | None = None
    apellido: str | None = None
    correo: str | None = None

class EnfermeraOut(EnfermeraBase):
    id: int

    class Config:
        orm_mode = True

# Y para Paciente
class PacienteBase(BaseModel):
    nombre: str
    apellido: str
    correo: str

class PacienteCreate(PacienteBase):
    pass

class PacienteUpdate(BaseModel):
    nombre: str | None = None
    apellido: str | None = None
    correo: str | None = None

class PacienteOut(PacienteBase):
    id: int

    class Config:
        orm_mode = True
