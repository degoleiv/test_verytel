from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date, LargeBinary

from app.config.database.base import Base

class Ciudadano(Base):
    __tablename__ = 'ciudadanos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    identificacion = Column(String(50), unique=True, nullable=False)
    correo = Column(String(100), nullable=False)
    celular = Column(String(20), nullable=False)
    barrio = Column(String(100), nullable=False)
    direccion = Column(String(200), nullable=False)
    frente_seguridad_id = Column(Integer, ForeignKey('frentes_seguridad.id'), nullable=False)
    tipo_documento = Column(String(10), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    sexo = Column(String(30), nullable=False)
    antecedentes = Column(Boolean, nullable=False)
    justificacion_antecedentes = Column(String, nullable=True)
    foto = Column(LargeBinary, nullable=True)
    usuario_verificado = Column(Boolean, default=False, nullable=False)
    codigo_verificacion = Column(String(6))
