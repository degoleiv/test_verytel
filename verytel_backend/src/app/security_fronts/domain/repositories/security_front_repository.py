from abc import ABC, abstractmethod
from typing import List, Optional
from app.security_fronts.domain.entities.security_front import FrenteSeguridad
class SecurityFrontRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[FrenteSeguridad]:
        pass

    @abstractmethod
    def get_by_id(self, frente_id: int) -> Optional[FrenteSeguridad]:
        pass

    @abstractmethod
    def create(self, frente: FrenteSeguridad) -> FrenteSeguridad:
        pass

    @abstractmethod
    def update(self, frente_id: int, nombre: str = None, descripcion: str = None) -> Optional[FrenteSeguridad]:
        pass

    @abstractmethod
    def delete(self, frente_id: int) -> Optional[FrenteSeguridad]:
        pass
