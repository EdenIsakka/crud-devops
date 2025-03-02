from pydantic import BaseModel, EmailStr
from typing import Optional

class DoctorSchema(BaseModel): #Validacion automatica 
    txtNombre: str
    txtCorreo: EmailStr #Verifica que el email sea valido.
    txtFoto: Optional[str] = None #Opcional, puede estar vacio el campo
