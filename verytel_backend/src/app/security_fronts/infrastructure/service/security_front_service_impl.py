from typing import List, Optional
from app.security_fronts.application.dto.security_front_dto import SecurityFrontDTO
from app.security_fronts.domain.repositories.security_front_repository import SecurityFrontRepository
from app.security_fronts.domain.entities.security_front import FrenteSeguridad
from app.security_fronts.application.services.security_front_service import SecurityFrontService

class SecurityFrontServiceImpl(SecurityFrontService):
    def __init__(self, repository: SecurityFrontRepository):
        # Inicia la clase con el repositorio de frentes de seguridad.
        self.repository = repository

    def register(self, dto: SecurityFrontDTO) -> bool:
        """Registrar un nuevo frente de seguridad."""
        # Convierte el DTO en una entidad (objeto del modelo de dominio).
        entity = FrenteSeguridad(
            nombre=dto.nombre,
            descripcion=dto.descripcion
        )
        # Usa el repositorio para crear la nueva entidad en la base de datos.
        created = self.repository.create(entity)
        # Devuelve True si la creación fue exitosa, de lo contrario, False.
        return created is not None

    def get_all(self) -> List[SecurityFrontDTO]:
        """Obtener todos los frentes de seguridad."""
        # Obtiene todos los frentes de seguridad desde el repositorio.
        entities = self.repository.get_all()
        # Convierte las entidades obtenidas en DTOs para ser devueltos.
        return [SecurityFrontDTO.from_orm(e) for e in entities]

    def get_by_id(self, frente_id: int) -> Optional[SecurityFrontDTO]:
        """Obtener un frente de seguridad por ID."""
        # Busca un frente de seguridad en el repositorio por su ID.
        entity = self.repository.get_by_id(frente_id)
        if entity:
            # Si encuentra el frente, lo convierte a DTO y lo retorna.
            return SecurityFrontDTO.from_orm(entity)
        # Si no lo encuentra, retorna None.
        return None

    def update(self, frente_id: int, dto: SecurityFrontDTO) -> bool:
        """Actualizar un frente de seguridad."""
        # Usa el repositorio para actualizar el frente de seguridad con el nuevo nombre y descripción.
        updated = self.repository.update(frente_id, dto.nombre, dto.descripcion)
        # Retorna True si el frente fue actualizado correctamente, False en caso contrario.
        return updated is not None

    def delete(self, frente_id: int) -> bool:
        """Eliminar un frente de seguridad."""
        # Usa el repositorio para eliminar el frente de seguridad con el ID proporcionado.
        deleted = self.repository.delete(frente_id)
        # Retorna True si el frente fue eliminado correctamente, False en caso contrario.
        return deleted is not None
