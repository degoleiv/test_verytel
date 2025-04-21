import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

class EmailConnectionFactory:
    email_connection = None
    
    @classmethod
    def initialize_connection_pool(cls, minconn: int = 1, maxconn: int = 5):
        """Inicializa la conexión SMTP"""
        if cls.email_connection is None:
            # Establecemos la conexión SMTP
            cls.email_connection = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
            cls.email_connection.login(SMTP_USERNAME, SMTP_PASSWORD)

    @classmethod
    def get_session(cls):
        """Obtiene la sesión para enviar correos"""
        if cls.email_connection is None:
            raise Exception("Connection pool not initialized")
        print("Getting session from pool")
        return cls.email_connection

    @classmethod
    def close_all_connections(cls):
        """Cierra la sesión SMTP cuando no sea necesaria"""
        if cls.email_connection is not None:
            cls.email_connection.quit()
            cls.email_connection = None
