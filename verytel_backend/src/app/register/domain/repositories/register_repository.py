

from abc import ABC, abstractmethod
class RegisterRepository(ABC):
    @abstractmethod
    def register_user(self, username: str, password: str) -> str:
        """
        Register a new user with the given username and password.
        Returns True if registration is successful, False otherwise.
        """
        pass

    @abstractmethod
    def check_username_exists(self, username: str) -> bool:
        """
        Check if the given username already exists in the system.
        Returns True if it exists, False otherwise.
        """
        pass
    @abstractmethod
    def check_validation_code(self,id, validation: str) -> bool:
        pass
    