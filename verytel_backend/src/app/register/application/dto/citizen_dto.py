# app/register/application/dto/citizen_dto.py

from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

class CitizenDTO(BaseModel):
    nombres: str
    apellidos: str
    identificacion: str
    correo: EmailStr
    celular: str
    barrio: str
    direccion: str
    frente_seguridad_id: int
    tipo_documento: str
    fecha_nacimiento: date
    sexo: str
    antecedentes: bool
    justificacion_antecedentes: Optional[str] = None
    foto: Optional[bytes] = None

    class Config:
        from_attributes = True