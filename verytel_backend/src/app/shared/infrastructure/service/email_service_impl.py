from app.shared.application.service.email_service import EmailService
from app.config.email.email_connection_factory import EmailConnectionFactory
from app.shared.infrastructure.repositories.email_repository import EmailRespository
from email.message import EmailMessage
class EmailServiceImpl(EmailService):
    def __init__(self):
        self.connection = EmailConnectionFactory.get_session()
        
    def send_verification_email(self, to_email: str, code: str):
        subject, content = EmailRespository.get_verification_email_content(code)
        message = EmailMessage()
        message["From"] = "catproyect1@gmail.com"
        message["To"] = to_email
        message["Subject"] = subject
        message.set_content(content)

        try:
            self.connection.send_message(message)
            print("Correo enviado correctamente")
            return True
        except Exception as e:
            print(f"Error al enviar correo: {e}")
            return False
                
        