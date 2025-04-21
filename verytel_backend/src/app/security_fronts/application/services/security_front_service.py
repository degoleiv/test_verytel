from abc import ABC, abstractmethod
from typing import List, Optional
from app.security_fronts.application.dto.security_front_dto import SecurityFrontDTO

class SecurityFrontService(ABC):
    
    @abstractmethod
    def register(self, dto: SecurityFrontDTO) -> bool:
        pass

    @abstractmethod
    def get_all(self) -> List[SecurityFrontDTO]:
        pass

    @abstractmethod
    def get_by_id(self, frente_id: int) -> Optional[SecurityFrontDTO]:
        pass

    @abstractmethod
    def update(self, frente_id: int, dto: SecurityFrontDTO) -> bool:
        pass

    @abstractmethod
    def delete(self, frente_id: int) -> bool:
        pass
