
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

# Define una clase 'SecurityFrontDTO' que hereda de 'BaseModel' de Pydantic.
# Esta clase representa un objeto de transferencia de datos (DTO) para la seguridad de un frente.
class SecurityFrontDTO(BaseModel):
    # El campo 'id' es opcional, y si no se proporciona, tomará el valor por defecto 'None'.
    id: Optional[int] = None 
    
    # El campo 'nombre' es obligatorio y tiene un máximo de 100 caracteres.
    nombre: str = Field(..., max_length=100)
    
    # El campo 'descripcion' es opcional (puede ser None) y tiene un máximo de 255 caracteres.
    descripcion: str | None = Field(default=None, max_length=255)
    
    # Configura la clase para permitir que los datos sean tratados como atributos de la clase.
    # 'from_attributes=True' indica que los datos de entrada se deben mapear desde atributos del objeto.
    model_config = ConfigDict(from_attributes=True)
