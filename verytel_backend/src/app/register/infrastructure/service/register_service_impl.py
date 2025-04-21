# app/infrastructure/services/register_service_impl.py
from app.register.application.services.register_service import RegisterService
from app.register.domain.repositories.register_repository import RegisterRepository
from app.register.application.dto.citizen_dto import CitizenDTO
from app.register.domain.entities.citizen import Ciudadano
from app.shared.application.service.email_service import EmailService
class RegisterServiceImpl(RegisterService):
    
    def __init__(self, register_repository: RegisterRepository, email: EmailService):
        self.register_repository = register_repository
        self.email_sender = email
    def register(self, citizen_dto: CitizenDTO) -> str:
        """
        Convierte el DTO en un modelo ORM y registra al ciudadano.
        """
       
        citizen = Ciudadano(
            nombres=citizen_dto.nombres,
            apellidos=citizen_dto.apellidos,
            identificacion=citizen_dto.identificacion,
            correo=citizen_dto.correo,
            celular=citizen_dto.celular,
            barrio=citizen_dto.barrio,
            direccion=citizen_dto.direccion,
            frente_seguridad_id=citizen_dto.frente_seguridad_id,
            tipo_documento=citizen_dto.tipo_documento,
            fecha_nacimiento=citizen_dto.fecha_nacimiento,
            sexo=citizen_dto.sexo,
            antecedentes=citizen_dto.antecedentes,
            justificacion_antecedentes=citizen_dto.justificacion_antecedentes,
            foto=citizen_dto.foto
        )
        
        code = self.register_repository.register_user(citizen)
        if code :  
            self.email_sender.send_verification_email(citizen.correo, code)
            return True
        return False

    def check_validation_code(self,id,  validation: str) -> bool:
        return self.register_repository.check_validation_code(id,validation)