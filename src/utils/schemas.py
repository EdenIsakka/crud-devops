from pydantic import BaseModel, EmailStr
from typing import Optional

class DoctorSchema(BaseModel): #Validacion automatica 
    nombre: str
    correo: EmailStr #Verifica que el email sea valido.
    foto: Optional[str] = None #Opcional, puede estar vacio el campo
