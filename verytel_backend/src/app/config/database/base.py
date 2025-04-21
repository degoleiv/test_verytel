# Importa la función 'declarative_base' del módulo 'sqlalchemy.orm'.
# Esta función se usa para crear una clase base desde la cual se definirán los modelos (tablas) de SQLAlchemy.
from sqlalchemy.orm import declarative_base

# Crea una clase base llamada 'Base' usando 'declarative_base()'.
# Todas las clases que representen tablas de la base de datos deben heredar de esta base.
Base = declarative_base()
