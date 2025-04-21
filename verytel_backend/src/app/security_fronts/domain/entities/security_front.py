from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.config.database.base import Base

# Define una clase 'FrenteSeguridad' que hereda de 'Base'.
# Esta clase mapea a la tabla 'frentes_seguridad' en la base de datos.
class FrenteSeguridad(Base):
    
    # Especifica el nombre de la tabla en la base de datos.
    __tablename__ = 'frentes_seguridad'
    
    # Define la columna 'id', que es de tipo 'Integer', clave primaria, y autoincremental.
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Define la columna 'nombre', que es de tipo 'String' con un máximo de 100 caracteres y no puede ser nula.
    nombre = Column(String(100), nullable=False)
    
    # Define la columna 'descripcion', que es de tipo 'String' con un máximo de 255 caracteres y puede ser nula.
    descripcion = Column(String(255), nullable=True)
    
    # Configura la clase para que Pydantic use este modelo en modo ORM (Object-Relational Mapping).
    # Esto permite que el modelo sea compatible con los esquemas de Pydantic para validación y serialización.
    class Config:
        orm_mode = True
