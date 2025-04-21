from app.register.domain.repositories.register_repository import RegisterRepository
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import and_
from app.register.domain.entities.citizen  import Ciudadano
import random
class RegisterRepositoryImpl(RegisterRepository):
    
    def __init__(self, db: Session):
        self.db = db  # `db` es ahora una sesión de SQLAlchemy
        
    def register_user(self, citizen: Ciudadano) -> str:
        """
        Register a new citizen with the given information.
        Returns True if registration is successful, False otherwise.
        """
       
        if self.check_username_exists(citizen.correo, citizen.identificacion):
            print("El correo o la identificación ya existen.")
            return None

        try:
            citizen.codigo_verificacion = f"{random.randint(100000, 999999)}"
            self.db.add(citizen)  # Agrega el ciudadano a la sesión
            self.db.commit()  # Guarda los cambios en la base de datos
            return  citizen.codigo_verificacion
        except IntegrityError as e:
            print("Error de integridad: el correo o la identificación ya existen." + str(e))
            # Si ocurre un error de integridad, como un usuario duplicado
            self.db.rollback()  # Deshace los cambios
            return  None

    def check_username_exists(self, correo: str, identificacion: str) -> bool:
      
        user = self.db.query(Ciudadano).filter(
            (Ciudadano.correo == correo) | (Ciudadano.identificacion == identificacion)
        ).first()
        return user is not None
    
    
    def check_validation_code(self,id, validation: str) -> bool:
          
        
        verification = self.db.query(Ciudadano).filter(
            and_(
                Ciudadano.codigo_verificacion == validation,
                Ciudadano.identificacion == id
            )
        ).first()
        
        if verification is None :
            return None
        
        if verification.usuario_verificado:
            return False 
        
        verification.usuario_verificado = True
        self.db.commit()
        self.db.refresh(verification)
        return True
