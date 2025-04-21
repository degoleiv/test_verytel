
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime as dt, timedelta, timezone  
from app.config.database.base import Base 
# Definimos la clase ValidationCode que mapea a la tabla 'validation_codes' en la base de datos
class ValidationCode(Base):
    __tablename__ = "validation_codes"  # Nombre de la tabla en la base de datos
    
    # Definición de los campos de la tabla y sus características
    id = Column(Integer, primary_key=True)  # Clave primaria de la tabla
    code = Column(String, nullable=False)  # Código de validación, no puede ser nulo
    user_id = Column(Integer, ForeignKey('ciudadanos.id'), nullable=False)  # Clave foránea hacia la tabla 'ciudadanos', no puede ser nula
    
    created_at = Column(DateTime, default=dt.now(timezone.utc))  # Fecha de creación del código, por defecto la fecha y hora actual en UTC
    expires_at = Column(DateTime)  # Fecha de expiración del código

    # Método para verificar si el código ha expirado
    def is_expired(self):
        now = dt.now(timezone.utc)  # Obtenemos la fecha y hora actual en UTC (datetime "aware" en UTC)
        exp = self.expires_at  # Fecha de expiración del código

        # Si expires_at es naive (sin timezone), lo forzamos a UTC
        if exp.tzinfo is None:
            exp = exp.replace(tzinfo=timezone.utc)

        print(f"{now} > {exp}")  # Imprimimos el valor actual y la fecha de expiración para depuración
        return now > exp  # Comprobamos si la fecha actual es mayor que la de expiración (es decir, el código ha expirado)
