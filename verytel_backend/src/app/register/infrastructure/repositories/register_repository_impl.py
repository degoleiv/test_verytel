# Importación de las dependencias necesarias
from app.register.domain.repositories.register_repository import RegisterRepository  # Se importa el repositorio base
from sqlalchemy.orm import Session  # Se importa para trabajar con las sesiones de SQLAlchemy
from sqlalchemy.exc import IntegrityError  # Se importa para manejar errores de integridad en las transacciones
from sqlalchemy import and_  # Se importa para combinar condiciones en las consultas SQL
from app.register.domain.entities.citizen import Ciudadano  # Se importa el modelo Ciudadano
import random  # Se importa para generar valores aleatorios, aunque no se usa en este código
from typing import List  # Se importa para definir tipos de retorno como listas

# Implementación del repositorio que interactúa con la base de datos usando SQLAlchemy
class RegisterRepositoryImpl(RegisterRepository):
    
    def __init__(self, db: Session):
        # Se inicializa el repositorio con una sesión de base de datos (db)
        self.db = db  # `db` es ahora una sesión de SQLAlchemy
        
    def register_user(self, citizen: Ciudadano) -> str:
        """
        Registra un nuevo ciudadano en la base de datos.
        Retorna el ID generado si es exitoso, o None si ocurre un error (por ejemplo, un duplicado).
        """
       
        # Comprobamos si el correo o la identificación ya existen en la base de datos
        if self.check_username_exists(citizen.correo, citizen.identificacion) is not None:
            print("El correo o la identificación ya existen.")
            return None

        try:
            # Agregamos el nuevo ciudadano a la base de datos
            self.db.add(citizen)
            # Confirmamos la transacción
            self.db.commit()
            # Actualizamos el objeto con el ID generado por la base de datos
            self.db.refresh(citizen)
            # Retornamos el ID del ciudadano registrado
            return citizen.id
        except IntegrityError as e:
            # Si ocurre un error de integridad (como un duplicado), lo manejamos
            print("Error de integridad: el correo o la identificación ya existen.\n" + str(e))
            self.db.rollback()  # Hacemos rollback para deshacer la transacción fallida
            return None

    def check_username_exists(self, correo: str, identificacion: str) -> bool:
        """
        Verifica si el correo o la identificación del ciudadano ya existen en la base de datos.
        Retorna True si alguno de los dos ya existe, False en caso contrario.
        """
        # Realizamos una consulta para verificar si existe un ciudadano con el correo o la identificación especificados
        user = self.db.query(Ciudadano).filter(
            (Ciudadano.correo == correo) | (Ciudadano.identificacion == identificacion)
        ).first()
        # Retorna True si encontramos un usuario, False si no
        return user 
    
    def check_validation_code(self, id) -> bool:
        """
        Marca a un ciudadano como verificado al comprobar su código de validación.
        """
        citizen = self.get_user(id)
        citizen.usuario_verificado = True  # Cambiamos el estado de verificación
        self.db.commit()  # Confirmamos los cambios en la base de datos
        self.db.refresh(citizen)  # Actualizamos el objeto para reflejar los cambios
        return True
    
    def get_user(self, id: str) -> Ciudadano:
        """
        Obtiene un ciudadano por su ID.
        """
        return self.db.query(Ciudadano).filter(
            (Ciudadano.id == id)  # Filtramos por el ID del ciudadano
        ).first()

    def get_user_by_verification(self, verification: str) -> List[Ciudadano]:
        """
        Obtiene todos los ciudadanos que tienen un estado de verificación especificado.
        """
        if verification in ["todos", ""]:
            return self.db.query(Ciudadano).all()
        
        elif verification == "verificado":
            return self.db.query(Ciudadano).filter(Ciudadano.usuario_verificado.is_(True)).all()
        
        elif verification == "no-verificado":
            return self.db.query(Ciudadano).filter(Ciudadano.usuario_verificado.is_(False)).all()
        
        # Si llega un valor no esperado, podrías devolver todo o lanzar una excepción
        return []