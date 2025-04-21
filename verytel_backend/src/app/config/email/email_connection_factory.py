# Importa el módulo smtplib, que permite enviar correos electrónicos usando el protocolo SMTP.
import smtplib

# Importa EmailMessage, una clase para construir correos electrónicos fácilmente.
from email.message import EmailMessage

# Importa load_dotenv para cargar variables de entorno desde un archivo .env.
from dotenv import load_dotenv

# Importa el módulo os para acceder a las variables de entorno del sistema.
import os

# Carga las variables de entorno definidas en el archivo .env al entorno de ejecución.
load_dotenv()

# Obtiene el valor de la variable de entorno SMTP_SERVER (servidor SMTP).
SMTP_SERVER = os.getenv("SMTP_SERVER")

# Obtiene el valor de SMTP_PORT y lo convierte a entero.
SMTP_PORT = int(os.getenv("SMTP_PORT"))

# Obtiene el nombre de usuario para autenticarse en el servidor SMTP.
SMTP_USERNAME = os.getenv("SMTP_USERNAME")

# Obtiene la contraseña correspondiente al nombre de usuario.
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

# Clase encargada de gestionar la conexión SMTP para el envío de correos.
class EmailConnectionFactory:
    # Variable de clase que mantiene la conexión SMTP activa.
    email_connection = None

    @classmethod
    def initialize_connection_pool(cls, minconn: int = 1, maxconn: int = 5):
        """Inicializa la conexión SMTP"""
        # Si no hay conexión SMTP creada aún...
        if cls.email_connection is None:
            # Crea una conexión segura usando SMTP sobre SSL al servidor y puerto especificados.
            cls.email_connection = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)

            # Inicia sesión con las credenciales proporcionadas.
            cls.email_connection.login(SMTP_USERNAME, SMTP_PASSWORD)

    @classmethod
    def get_session(cls):
        """Obtiene la sesión para enviar correos"""
        # Si la conexión aún no ha sido inicializada, lanza una excepción.
        if cls.email_connection is None:
            raise Exception("Connection pool not initialized")

        # Imprime un mensaje en consola indicando que se obtuvo la sesión SMTP.
        print("Getting session from pool")

        # Devuelve la conexión SMTP activa.
        return cls.email_connection

    @classmethod
    def close_all_connections(cls):
        """Cierra la sesión SMTP cuando no sea necesaria"""
        # Si existe una conexión activa...
        if cls.email_connection is not None:
            # Cierra la conexión SMTP de forma adecuada.
            cls.email_connection.quit()

            # Limpia la referencia a la conexión.
            cls.email_connection = None
