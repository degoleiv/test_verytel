# Importamos las clases necesarias para la definición de la entidad 'Ciudadano' y las funcionalidades del repositorio
from app.register.domain.entities.citizen import Ciudadano
from abc import ABC, abstractmethod  # Importamos para definir clases y métodos abstractos
from typing import List  # Importamos List para definir tipos de listas

# Definimos la interfaz 'RegisterRepository', que servirá como repositorio para las operaciones relacionadas con el registro de usuarios
class RegisterRepository(ABC):
    # Método abstracto para registrar un nuevo usuario con nombre de usuario y contraseña
    @abstractmethod
    def register_user(self, username: str, password: str) -> str:
        """
        Registra un nuevo usuario con el nombre de usuario y contraseña proporcionados.
        Retorna el ID del usuario registrado si el registro es exitoso, o un mensaje de error en caso contrario.
        """
        pass

    # Método abstracto para verificar si un nombre de usuario ya existe en el sistema
    @abstractmethod
    def check_username_exists(self, correo: str, identificacion: str) -> bool:
        """
        Verifica si el nombre de usuario dado ya existe en el sistema.
        Retorna True si ya existe, False en caso contrario.
        """
        pass

    # Método abstracto para verificar el código de validación de un usuario
    @abstractmethod
    def check_validation_code(self, id, validation: bool) -> bool:
        """
        Verifica si el código de validación para el usuario es correcto.
        Retorna True si es válido, False en caso contrario.
        """
        pass

    # Método abstracto para obtener los detalles de un usuario a partir de su ID
    @abstractmethod
    def get_user(self, id: str) -> Ciudadano:
        """
        Obtiene los detalles de un usuario a partir de su ID.
        Retorna un objeto de tipo 'Ciudadano' que contiene la información del usuario.
        """
        pass

    # Método abstracto para obtener una lista de usuarios verificados o no verificados
    @abstractmethod
    def get_user_by_verification(self, verification: str) -> List[Ciudadano]:
        """
        Obtiene una lista de usuarios en función de su estado de verificación.
        Retorna una lista de objetos de tipo 'Ciudadano' que están verificados o no verificados.
        """
        pass
