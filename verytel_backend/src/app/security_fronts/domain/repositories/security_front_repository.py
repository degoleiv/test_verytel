
from abc import ABC, abstractmethod
from typing import List, Optional
from app.security_fronts.domain.entities.security_front import FrenteSeguridad

# Define una clase abstracta llamada 'SecurityFrontRepository' que hereda de 'ABC'.
# Esta clase representa un repositorio abstracto para manejar la persistencia de los frentes de seguridad.
class SecurityFrontRepository(ABC):

    # Método abstracto para obtener todos los frentes de seguridad.
    # Retorna una lista de objetos 'FrenteSeguridad'.
    @abstractmethod
    def get_all(self) -> List[FrenteSeguridad]:
        pass

    # Método abstracto para obtener un frente de seguridad por su ID.
    # Recibe el ID del frente como parámetro y retorna un objeto 'FrenteSeguridad' o None.
    @abstractmethod
    def get_by_id(self, frente_id: int) -> Optional[FrenteSeguridad]:
        pass

    # Método abstracto para crear un nuevo frente de seguridad.
    # Recibe un objeto 'FrenteSeguridad' como parámetro y retorna el objeto creado.
    @abstractmethod
    def create(self, frente: FrenteSeguridad) -> FrenteSeguridad:
        pass

    # Método abstracto para actualizar un frente de seguridad.
    # Recibe el ID del frente y los parámetros opcionales de nombre y descripción.
    # Retorna un objeto 'FrenteSeguridad' actualizado o None si no se encuentra el frente.
    @abstractmethod
    def update(self, frente_id: int, nombre: str = None, descripcion: str = None) -> Optional[FrenteSeguridad]:
        pass

    # Método abstracto para eliminar un frente de seguridad.
    # Recibe el ID del frente a eliminar y retorna el objeto 'FrenteSeguridad' eliminado o None.
    @abstractmethod
    def delete(self, frente_id: int) -> Optional[FrenteSeguridad]:
        pass
