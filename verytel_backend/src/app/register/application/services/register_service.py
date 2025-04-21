# app/register/application/services/register_service.py
from abc import ABC, abstractmethod
from app.register.application.dto.citizen_dto import CitizenDTO

class RegisterService(ABC):
    
    @abstractmethod
    def register(self, citizen_dto: CitizenDTO) -> str:
        """
        Método abstracto para registrar un ciudadano.
        """
        pass
    
    @abstractmethod
    def check_validation_code(self,id, validation: str) -> bool:
        pass