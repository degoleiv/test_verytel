# Importación de clases y funciones necesarias
from abc import ABC, abstractmethod  # Se importa para definir clases y métodos abstractos
from typing import Optional  # Se importa para manejar valores que pueden ser None
from datetime import datetime  # Se importa para trabajar con fechas y horas

# Definimos la interfaz 'ValidationCodeRepository', que sirve para manejar las operaciones relacionadas con los códigos de validación
class ValidationCodeRepository(ABC):
    
    # Método abstracto para registrar un nuevo código de validación para un usuario
    @abstractmethod
    def register_code(self , username: str) -> str:
        """
        Genera y guarda un nuevo código de validación para el usuario.
        Retorna el código generado.
        """
        pass

    # Método abstracto para obtener el código de validación actual de un usuario
    @abstractmethod
    def get_code(self, username: str) -> Optional[str]:
        """
        Obtiene el código de validación actual del usuario si existe y no está expirado.
        Retorna el código si existe, de lo contrario, retorna None.
        """
        pass
  
    # Método abstracto para refrescar el código de validación de un usuario
    @abstractmethod
    def refresh_code(self, user_id: int) -> bool:
        """
        Actualiza el código de validación de un usuario.
        Retorna True si se refresca exitosamente, False en caso contrario.
        """
        pass

    # Método abstracto para verificar si un código ha expirado
    @abstractmethod
    def is_code_expired(self, code: str, userid: str) -> bool:
        """
        Verifica si un código ha expirado para el usuario dado.
        Retorna True si el código ha expirado, False si no.
        """
        pass

    # Método abstracto para obtener la fecha de expiración de un código de validación
    @abstractmethod
    def get_expiration_time(self, code: str) -> Optional[datetime]:
        """
        Devuelve la fecha de expiración de un código.
        Retorna un objeto datetime si existe la fecha de expiración, de lo contrario, retorna None.
        """
        pass

    # Método abstracto para eliminar todos los códigos de validación expirados de la base de datos
    @abstractmethod
    def delete_expired_codes(self) -> int:
        """
        Elimina todos los códigos expirados de la base de datos.
        Retorna el número de códigos eliminados.
        """
        pass
