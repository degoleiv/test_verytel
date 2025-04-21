# app/security_fronts/application/services/security_front_service_impl.py
from typing import List, Optional
from app.security_fronts.application.dto.security_front_dto import SecurityFrontDTO
from app.security_fronts.domain.repositories.security_front_repository import SecurityFrontRepository
from app.security_fronts.domain.entities.security_front import FrenteSeguridad
from app.security_fronts.application.services.security_front_service import SecurityFrontService

class SecurityFrontServiceImpl(SecurityFrontService):
    def __init__(self, repository: SecurityFrontRepository):
        self.repository = repository

    def register(self, dto: SecurityFrontDTO) -> bool:
        """Registrar un nuevo frente de seguridad."""
        entity = FrenteSeguridad(
            nombre=dto.nombre,
            descripcion=dto.descripcion
        )
        created = self.repository.create(entity)
        return created is not None

    def get_all(self) -> List[SecurityFrontDTO]:
        """Obtener todos los frentes de seguridad."""
        entities = self.repository.get_all()
        return [SecurityFrontDTO.from_orm(e) for e in entities]

    def get_by_id(self, frente_id: int) -> Optional[SecurityFrontDTO]:
        """Obtener un frente de seguridad por ID."""
        entity = self.repository.get_by_id(frente_id)
        if entity:
            return SecurityFrontDTO.from_orm(entity)
        return None

    def update(self, frente_id: int, dto: SecurityFrontDTO) -> bool:
        """Actualizar un frente de seguridad."""
        updated = self.repository.update(frente_id, dto.nombre, dto.descripcion)
        return updated is not None

    def delete(self, frente_id: int) -> bool:
        """Eliminar un frente de seguridad."""
        deleted = self.repository.delete(frente_id)
        return deleted is not None
