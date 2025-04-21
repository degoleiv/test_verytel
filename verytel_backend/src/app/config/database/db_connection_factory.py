# db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()
ENGINE_URL = os.getenv("ENGINE_URL")

class DatabaseConnectionFactory:
    _engine = None
    _Session = None

    @classmethod
    def initialize_connection_pool(cls, minconn: int = 1, maxconn: int = 5):
        if cls._engine is None:
            engine_url =ENGINE_URL 
            cls._engine = create_engine(engine_url, pool_size=maxconn, max_overflow=0)
            cls._Session = sessionmaker(bind=cls._engine)

    @classmethod
    def get_session(cls):
        if cls._Session is None:
            raise Exception("Connection pool not initialized")
        print("Getting session from pool")
        return cls._Session()

    @classmethod
    def get_engine(cls):
        if cls._engine is None:
            raise Exception("Engine not initialized")
        return cls._engine

    @classmethod
    def close_all_connections(cls):
        if cls._engine is not None:
            cls._engine.dispose()
            cls._engine = None
