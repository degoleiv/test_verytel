
from sqlalchemy.orm import Session

from sqlalchemy.exc import SQLAlchemyError

from app.security_fronts.domain.repositories.security_front_repository import SecurityFrontRepository


from app.security_fronts.domain.entities.security_front import FrenteSeguridad


import logging


logger = logging.getLogger(__name__)

# Define la clase 'FrenteSeguridadRepositoryImpl' que implementa el repositorio para los frentes de seguridad.
class FrenteSeguridadRepositoryImpl(SecurityFrontRepository):
    # El constructor recibe una sesión de base de datos para interactuar con la base de datos.
    def __init__(self, db: Session):
        self.db = db

    # Método para obtener todos los frentes de seguridad desde la base de datos.
    def get_all(self):
        try:
            # Realiza una consulta a la base de datos para obtener todos los registros de la tabla 'FrenteSeguridad'.
            return self.db.query(FrenteSeguridad).all()
        except SQLAlchemyError as e:
            # Si ocurre un error en la consulta, lo registra en los logs y retorna una lista vacía.
            logger.error(f"Error al obtener todos los frentes: {e}")
            return []

    # Método para obtener un frente de seguridad por su ID.
    def get_by_id(self, frente_id: int):
        try:
            # Realiza una consulta para obtener un frente de seguridad por su ID.
            return self.db.query(FrenteSeguridad).filter(FrenteSeguridad.id == frente_id).first()
        except SQLAlchemyError as e:
            # Si ocurre un error, lo registra en los logs y retorna None.
            logger.error(f"Error al obtener frente con ID {frente_id}: {e}")
            return None

    # Método para crear un nuevo frente de seguridad.
    def create(self, frente: FrenteSeguridad):
        try:
            # Verifica si ya existe un frente con el mismo nombre.
            existente = self.db.query(FrenteSeguridad).filter_by(nombre=frente.nombre).first()
            if existente:
                # Si ya existe, registra una advertencia y retorna None.
                logger.warning(f"Ya existe un frente con el nombre: {frente.nombre}")
                return None

            # Si no existe, agrega el nuevo frente y realiza el commit en la base de datos.
            self.db.add(frente)
            self.db.commit()
            # Refresca el objeto para obtener los valores más recientes después del commit.
            self.db.refresh(frente)
            return frente
        except SQLAlchemyError as e:
            # Si ocurre un error, realiza un rollback y lo registra en los logs.
            self.db.rollback()
            logger.error(f"Error al crear frente: {e}")
            return None

    # Método para actualizar un frente de seguridad existente.
    def update(self, frente_id: int, nombre: str = None, descripcion: str = None):
        try:
            # Obtiene el frente de seguridad por su ID.
            frente = self.get_by_id(frente_id)
            if not frente:
                # Si no se encuentra el frente, registra una advertencia y retorna None.
                logger.warning(f"No se encontró el frente con ID {frente_id} para actualizar")
                return None

            # Si se proporciona un nuevo nombre, lo asigna al frente.
            if nombre is not None:
                frente.nombre = nombre
            # Si se proporciona una nueva descripción, la asigna al frente.
            if descripcion is not None:
                frente.descripcion = descripcion

            # Realiza el commit para guardar los cambios en la base de datos.
            self.db.commit()
            # Refresca el objeto para obtener los valores más recientes después del commit.
            self.db.refresh(frente)
            return frente
        except SQLAlchemyError as e:
            # Si ocurre un error, realiza un rollback y lo registra en los logs.
            self.db.rollback()
            logger.error(f"Error al actualizar frente con ID {frente_id}: {e}")
            return None

    # Método para eliminar un frente de seguridad.
    def delete(self, frente_id: int):
        try:
            # Obtiene el frente de seguridad por su ID.
            frente = self.get_by_id(frente_id)
            if not frente:
                # Si no se encuentra el frente, registra una advertencia y retorna None.
                logger.warning(f"No se encontró el frente con ID {frente_id} para eliminar")
                return None

            # Si se encuentra el frente, lo elimina y realiza el commit.
            self.db.delete(frente)
            self.db.commit()
            return frente
        except SQLAlchemyError as e:
            # Si ocurre un error, realiza un rollback y lo registra en los logs.
            self.db.rollback()
            logger.error(f"Error al eliminar frente con ID {frente_id}: {e}")
            return None
