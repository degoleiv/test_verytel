from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.config.database.base import Base
class FrenteSeguridad(Base):
    __tablename__ = 'frentes_seguridad'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(255), nullable=True)
    class Config:
        orm_mode = True
