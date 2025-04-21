
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date, LargeBinary
from app.config.database.base import Base 
# Definimos la clase Ciudadano que mapea a la tabla 'ciudadanos' en la base de datos
class Ciudadano(Base):
    __tablename__ = 'ciudadanos'  # Nombre de la tabla en la base de datos
    
    # Definición de los campos de la tabla y sus características
    id = Column(Integer, primary_key=True, autoincrement=True)  # Clave primaria con autoincremento
    nombres = Column(String(100), nullable=False)  # Nombre del ciudadano, no puede ser nulo
    apellidos = Column(String(100), nullable=False)  # Apellidos del ciudadano, no puede ser nulo
    identificacion = Column(String(50), unique=True, nullable=False)  # Identificación única del ciudadano, no puede ser nula
    correo = Column(String(100), nullable=False)  # Correo electrónico del ciudadano, no puede ser nulo
    celular = Column(String(20), nullable=False)  # Número de celular del ciudadano, no puede ser nulo
    barrio = Column(String(100), nullable=False)  # Barrio del ciudadano, no puede ser nulo
    direccion = Column(String(200), nullable=False)  # Dirección del ciudadano, no puede ser nulo
    frente_seguridad_id = Column(Integer, ForeignKey('frentes_seguridad.id'), nullable=False)  # Clave foránea hacia la tabla 'frentes_seguridad'
    tipo_documento = Column(String(10), nullable=False)  # Tipo de documento del ciudadano, no puede ser nulo
    fecha_nacimiento = Column(Date, nullable=False)  # Fecha de nacimiento del ciudadano, no puede ser nula
    sexo = Column(String(30), nullable=False)  # Sexo del ciudadano, no puede ser nulo
    antecedentes = Column(Boolean, nullable=False)  # Si tiene antecedentes o no, no puede ser nulo
    justificacion_antecedentes = Column(String, nullable=True)  # Justificación si tiene antecedentes, puede ser nula
    foto = Column(LargeBinary, nullable=True)  # Foto del ciudadano en formato binario, puede ser nula
    usuario_verificado = Column(Boolean, default=False, nullable=False)  # Si el usuario está verificado, por defecto es 'False'
