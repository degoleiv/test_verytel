# Importamos clases y módulos necesarios
from abc import ABC, abstractmethod  # Importamos ABC y abstractmethod para definir clases abstractas y métodos abstractos.
from app.register.application.dto.citizen_dto import CitizenDTO  # Importamos el DTO de Citizen para trabajar con los datos de ciudadanos.
from typing import List  # Importamos 'List' para indicar que el método puede recibir y devolver listas.

# Definimos un servicio abstracto para el registro de ciudadanos
class RegisterService(ABC):

    @abstractmethod
    def register(self, citizen_dto: CitizenDTO) -> str:
        """
        Método abstracto para registrar un ciudadano.
        Recibe un objeto CitizenDTO con los datos del ciudadano a registrar.
        Devuelve un mensaje o identificador (str) del registro realizado.
        """
        pass
    
    @abstractmethod
    def check_validation_code(self, id, validation: str) -> bool:
        """
        Método abstracto para verificar un código de validación.
        Recibe un ID de ciudadano y un código de validación.
        Devuelve un valor booleano indicando si la validación fue correcta.
        """
        pass
    
    @abstractmethod
    def refresh_code(self, id) -> bool:
        """
        Método abstracto para refrescar el código de validación de un ciudadano.
        Recibe un ID de ciudadano.
        Devuelve un valor booleano indicando si la operación fue exitosa.
        """
        pass
    
    @abstractmethod
    def register_bulk(self, users: List[CitizenDTO]) -> dict:
        """
        Método abstracto para registrar varios ciudadanos de una vez.
        Recibe una lista de objetos CitizenDTO.
        Devuelve un diccionario con los resultados del registro de los ciudadanos.
        """
        pass
    
    @abstractmethod
    def get_user_by_verification(self, verification: str) -> List[CitizenDTO]:
        """
        Método abstracto para obtener una lista de ciudadanos que han sido verificados o no.
        Recibe un valor booleano indicando si se busca usuarios verificados (True) o no verificados (False).
        Devuelve una lista de objetos CitizenDTO.
        """
        pass
