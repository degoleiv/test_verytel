
from app.shared.application.service.email_service import EmailService
from app.config.email.email_connection_factory import EmailConnectionFactory
from app.shared.infrastructure.repositories.email_repository import EmailRespository

from email.message import EmailMessage

# Define una clase 'EmailServiceImpl' que implementa la interfaz 'EmailService'.
# Esta clase proporciona la implementación concreta para enviar correos electrónicos de verificación.
class EmailServiceImpl(EmailService):
    
    # Método constructor que inicializa la conexión SMTP utilizando 'EmailConnectionFactory'.
    def __init__(self):
        # Establece la conexión SMTP llamando al método 'get_session' de 'EmailConnectionFactory'.
        self.connection = EmailConnectionFactory.get_session()

    # Implementación del método 'send_verification_email' para enviar un correo de verificación.
    # Recibe como parámetros la dirección de correo del destinatario y el código de verificación.
    def send_verification_email(self, to_email: str, code: str):
        # Obtiene el asunto y el contenido del correo usando el método estático de 'EmailRespository'.
        subject, content = EmailRespository.get_verification_email_content(code)

        # Crea un nuevo mensaje de correo electrónico utilizando 'EmailMessage'.
        message = EmailMessage()

        # Establece la dirección de correo del remitente.
        message["From"] = "catproyect1@gmail.com"
        
        # Establece la dirección de correo del destinatario.
        message["To"] = to_email
        
        # Establece el asunto del mensaje.
        message["Subject"] = subject
        
        # Establece el contenido del mensaje (cuerpo del correo).
        message.set_content(content)

        try:
            # Intenta enviar el mensaje usando la conexión SMTP.
            self.connection.send_message(message)
            print("Correo enviado correctamente")
            # Retorna True si el correo se envió con éxito.
            return True
        except Exception as e:
            # En caso de error al enviar el correo, imprime el mensaje de error.
            print(f"Error al enviar correo: {e}")
            # Retorna False si hubo un error al enviar el correo.
            return False
