
# Importa la función create_engine para crear un motor de conexión a la base de datos.
from sqlalchemy import create_engine

# Importa sessionmaker, que se utiliza para crear instancias de sesión para interactuar con la base de datos.
from sqlalchemy.orm import sessionmaker

# Importa load_dotenv para cargar variables de entorno desde un archivo .env.
from dotenv import load_dotenv

# Importa el módulo os para acceder a las variables de entorno.
import os

# Cargar las variables de entorno definidas en un archivo .env en el entorno de ejecución.
load_dotenv()

# Obtener la URL del motor de base de datos desde las variables de entorno.
ENGINE_URL = os.getenv("ENGINE_URL")

# Define una clase de fábrica para gestionar la conexión a la base de datos y las sesiones.
class DatabaseConnectionFactory:
    # Variable de clase para almacenar el motor de conexión (engine).
    _engine = None

    # Variable de clase para almacenar el generador de sesiones (session factory).
    _Session = None

    # Método de clase para inicializar el pool de conexiones.
    # Recibe los parámetros opcionales minconn (mínimo de conexiones) y maxconn (máximo de conexiones).
    @classmethod
    def initialize_connection_pool(cls, minconn: int = 1, maxconn: int = 5):
        # Solo inicializa si el motor no ha sido creado previamente.
        if cls._engine is None:
            # Obtiene la URL del motor desde la variable de entorno cargada anteriormente.
            engine_url = ENGINE_URL

            # Crea el motor de conexión con SQLAlchemy utilizando la URL y configuración del pool.
            cls._engine = create_engine(engine_url, pool_size=maxconn, max_overflow=0)

            # Crea el generador de sesiones utilizando el motor.
            cls._Session = sessionmaker(bind=cls._engine)

    # Método de clase para obtener una nueva sesión desde el pool.
    @classmethod
    def get_session(cls):
        # Si la sesión aún no se ha inicializado, lanza una excepción.
        if cls._Session is None:
            raise Exception("Connection pool not initialized")

        # Muestra un mensaje en consola cuando se obtiene una sesión.
        print("Getting session from pool")

        # Retorna una nueva instancia de sesión.
        return cls._Session()

    # Método de clase para obtener el motor actual.
    @classmethod
    def get_engine(cls):
        # Si el motor aún no se ha inicializado, lanza una excepción.
        if cls._engine is None:
            raise Exception("Engine not initialized")

        # Retorna el motor actual.
        return cls._engine

    # Método de clase para cerrar todas las conexiones y limpiar el motor.
    @classmethod
    def close_all_connections(cls):
        # Si el motor existe, lo cierra y lo elimina.
        if cls._engine is not None:
            cls._engine.dispose()  # Cierra todas las conexiones del pool.
            cls._engine = None     # Establece el motor como None para evitar reutilización.
