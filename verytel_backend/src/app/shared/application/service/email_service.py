from abc import ABC, abstractmethod

# Define una clase abstracta llamada 'EmailService', que sirve como interfaz o contrato.
class EmailService(ABC):
    # Define un método abstracto que debe ser implementado por cualquier clase que herede de 'EmailService'.
    # Este método se usará para enviar un correo de verificación, recibiendo como parámetros el correo destino y un código.
    @abstractmethod
    def send_verification_email(self, to_email: str, code: str):
        pass  # Este método no tiene implementación aquí, solo define la firma del método.
