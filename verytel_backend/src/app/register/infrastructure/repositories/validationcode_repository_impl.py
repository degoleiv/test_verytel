# Importación de dependencias necesarias
from typing import Optional  # Se importa para usar tipos opcionales en las funciones
from sqlalchemy import and_  # Se importa para combinar condiciones en las consultas SQL
from app.register.domain.repositories.validationcode_repository import ValidationCodeRepository  # Importa el repositorio base
from sqlalchemy.orm import Session  # Importa la sesión de SQLAlchemy para interactuar con la base de datos
import secrets  # Se importa para generar valores aleatorios seguros (como tokens)
from datetime import datetime as dt, timedelta, timezone  # Se importa para trabajar con fechas y horas

from app.register.domain.entities.validation_codes import ValidationCode  # Importa el modelo de código de validación

# Implementación del repositorio de códigos de validación
class ValidationCodeRepositoryImpl(ValidationCodeRepository):
    
    def __init__(self, db: Session):
        # Se inicializa el repositorio con una sesión de base de datos (db)
        self.db = db

    def register_code(self, user_id: str) -> str:
        """
        Genera un nuevo código de validación para el usuario y lo guarda en la base de datos.
        """
        # Generar un nuevo código aleatorio con 6 caracteres hexadecimales
        code = secrets.token_hex(3)  # 6 caracteres hex
        # Definir la fecha de expiración del código (15 minutos desde ahora)
        expires_at = dt.now(timezone.utc) + timedelta(minutes=15)

        # Crear una nueva instancia de ValidationCode
        new_code = ValidationCode(
            user_id=user_id,
            code=code,
            expires_at=expires_at
        )
        
        # Agregar el nuevo código a la base de datos y confirmar la transacción
        self.db.add(new_code)
        self.db.commit()
        # Actualizar el objeto con los valores generados en la base de datos
        self.db.refresh(new_code)
        
        # Retornar el código generado
        return code

    def get_code(self, username: str) -> Optional[str]:
        """
        Obtiene el código de validación más reciente para un usuario, si no ha expirado.
        """
        # Obtener el ID del usuario a partir de su nombre de usuario
        user_id = self._get_user_id_by_username(username)
        if not user_id:
            return None  # Si no existe el usuario, retornar None

        # Buscar el código de validación más reciente para el usuario
        code_entry = (
            self.db.query(ValidationCode)
            .filter(ValidationCode.user_id == user_id)
            .order_by(ValidationCode.created_at.desc())  # Ordenar por fecha de creación descendente
            .first()
        )
        
        # Si no existe el código o está expirado, retornar None
        if not code_entry or code_entry.is_expired():
            return None

        # Retornar el código de validación si está disponible y no ha expirado
        return code_entry.code

    def refresh_code(self, user_id: int) -> bool:
        """
        Genera un nuevo código de validación para un usuario y actualiza el registro en la base de datos.
        """
        # Buscar el código más reciente para el usuario
        existing = (
            self.db.query(ValidationCode)
            .filter(ValidationCode.user_id == user_id)
            .order_by(ValidationCode.created_at.desc())
            .first()
        )
        
        if existing:
            # Generar un nuevo código y actualizar su fecha de expiración
            existing.code = secrets.token_hex(3)  # Generar un nuevo código
            existing.expires_at = dt.now(timezone.utc) + timedelta(minutes=15)  # Actualizar la expiración
            self.db.commit()  # Confirmar la transacción
            return existing.code  # Retornar el nuevo código
        return None  # Si no se encuentra un código existente, retornar None

    def is_code_expired(self, code: str, userid: str) -> bool:
        """
        Verifica si un código de validación ha expirado.
        """
        # Buscar el registro del código usando el código y el ID del usuario
        record = self.db.query(ValidationCode).filter(
            and_(
                ValidationCode.code == code,
                ValidationCode.user_id == userid
            )
        ).first()
        
        if not record:
            return None  # Si no se encuentra el registro, retornar None
        
        # Verificar si el código ha expirado usando el método is_expired del modelo
        return record.is_expired()

    def get_expiration_time(self, code: str) -> Optional[dt]:
        """
        Devuelve la fecha de expiración de un código de validación.
        """
        # Buscar el registro del código en la base de datos
        record = self.db.query(ValidationCode).filter_by(code=code).first()
        if record:
            return record.expires_at  # Retornar la fecha de expiración
        return None  # Si no se encuentra el código, retornar None

    def delete_expired_codes(self) -> int:
        """
        Elimina todos los códigos de validación que han expirado de la base de datos.
        """
        # Obtener la fecha y hora actual en UTC
        now = dt.now(timezone.utc)
        # Eliminar todos los registros de códigos expirados
        deleted = (
            self.db.query(ValidationCode)
            .filter(ValidationCode.expires_at < now)  # Filtrar por códigos expirados
            .delete(synchronize_session=False)  # Eliminar sin sincronizar la sesión
        )
        self.db.commit()  # Confirmar la transacción
        return deleted  # Retornar el número de registros eliminados
