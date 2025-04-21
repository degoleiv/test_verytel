from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.security_fronts.domain.repositories.security_front_repository import SecurityFrontRepository
from app.security_fronts.domain.entities.security_front import FrenteSeguridad
import logging

logger = logging.getLogger(__name__)

class FrenteSeguridadRepositoryImpl(SecurityFrontRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        try:
            return self.db.query(FrenteSeguridad).all()
        except SQLAlchemyError as e:
            logger.error(f"Error al obtener todos los frentes: {e}")
            return []

    def get_by_id(self, frente_id: int):
        try:
            return self.db.query(FrenteSeguridad).filter(FrenteSeguridad.id == frente_id).first()
        except SQLAlchemyError as e:
            logger.error(f"Error al obtener frente con ID {frente_id}: {e}")
            return None

    def create(self, frente: FrenteSeguridad):
        try:
            existente = self.db.query(FrenteSeguridad).filter_by(nombre=frente.nombre).first()
            if existente:
                logger.warning(f"Ya existe un frente con el nombre: {frente.nombre}")
                return None
            self.db.add(frente)
            self.db.commit()
            self.db.refresh(frente)
            return frente
        except SQLAlchemyError as e:
            self.db.rollback()
            logger.error(f"Error al crear frente: {e}")
            return None

    def update(self, frente_id: int, nombre: str = None, descripcion: str = None):
        try:
            frente = self.get_by_id(frente_id)
            if not frente:
                logger.warning(f"No se encontró el frente con ID {frente_id} para actualizar")
                return None

            if nombre is not None:
                frente.nombre = nombre
            if descripcion is not None:
                frente.descripcion = descripcion

            self.db.commit()
            self.db.refresh(frente)
            return frente
        except SQLAlchemyError as e:
            self.db.rollback()
            logger.error(f"Error al actualizar frente con ID {frente_id}: {e}")
            return None

    def delete(self, frente_id: int):
        try:
            frente = self.get_by_id(frente_id)
            if not frente:
                logger.warning(f"No se encontró el frente con ID {frente_id} para eliminar")
                return None

            self.db.delete(frente)
            self.db.commit()
            return frente
        except SQLAlchemyError as e:
            self.db.rollback()
            logger.error(f"Error al eliminar frente con ID {frente_id}: {e}")
            return None
