from abc import ABC, abstractmethod
from typing import List, Optional
from app.security_fronts.application.dto.security_front_dto import SecurityFrontDTO

# Define una clase abstracta llamada 'SecurityFrontService' que hereda de 'ABC'.
# Esta clase define una interfaz para gestionar operaciones sobre los frentes de seguridad.
class SecurityFrontService(ABC):
    
    # Método abstracto para registrar un nuevo frente de seguridad.
    # Debe recibir un objeto 'SecurityFrontDTO' y retornar un valor booleano.
    @abstractmethod
    def register(self, dto: SecurityFrontDTO) -> bool:
        pass

    # Método abstracto para obtener todos los frentes de seguridad.
    # Retorna una lista de objetos 'SecurityFrontDTO'.
    @abstractmethod
    def get_all(self) -> List[SecurityFrontDTO]:
        pass

    # Método abstracto para obtener un frente de seguridad por su ID.
    # Recibe el ID del frente como parámetro y retorna un objeto 'SecurityFrontDTO' o None.
    @abstractmethod
    def get_by_id(self, frente_id: int) -> Optional[SecurityFrontDTO]:
        pass

    # Método abstracto para actualizar un frente de seguridad.
    # Recibe el ID del frente y un objeto 'SecurityFrontDTO' con los nuevos datos.
    # Retorna un valor booleano para indicar si la actualización fue exitosa.
    @abstractmethod
    def update(self, frente_id: int, dto: SecurityFrontDTO) -> bool:
        pass

    # Método abstracto para eliminar un frente de seguridad.
    # Recibe el ID del frente a eliminar y retorna un valor booleano indicando el éxito de la operación.
    @abstractmethod
    def delete(self, frente_id: int) -> bool:
        pass
