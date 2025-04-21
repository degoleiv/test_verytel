from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
class SecurityFrontDTO(BaseModel):
    id: Optional[int] = None 
    nombre: str = Field(..., max_length=100)
    descripcion: str | None = Field(default=None, max_length=255)
    model_config = ConfigDict(from_attributes=True)