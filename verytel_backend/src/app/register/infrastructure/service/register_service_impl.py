from app.register.application.services.register_service import RegisterService
from app.register.domain.repositories.register_repository import RegisterRepository
from app.register.application.dto.citizen_dto import CitizenDTO
from app.register.domain.entities.citizen import Ciudadano
from app.shared.application.service.email_service import EmailService
from app.register.domain.repositories.validationcode_repository import ValidationCodeRepository
from typing import List

# Implementación del servicio de registro
class RegisterServiceImpl(RegisterService):
    
    def __init__(self, 
                 register_repository: RegisterRepository, 
                 email: EmailService,
                 code : ValidationCodeRepository ):
        """
        Constructor que inyecta las dependencias necesarias para el servicio de registro.
        - **register_repository**: Repositorio para interactuar con la base de datos para el registro de ciudadanos.
        - **email**: Servicio de correo para enviar correos electrónicos.
        - **code**: Repositorio para la gestión de códigos de verificación.
        """
        self.register_repository = register_repository  # Repositorio para el registro de usuarios
        self.email_sender = email  # Servicio de correo para el envío de emails
        self.code = code  # Repositorio para manejar los códigos de validación

    def register(self, citizen_dto: CitizenDTO) -> str:
        """
        Convierte el DTO en un modelo ORM (Ciudadano) y lo registra en la base de datos.
        Luego genera un código de validación y envía un correo al usuario.
        - **citizen_dto**: Objeto DTO que contiene los datos del ciudadano.
        
        Retorna True si el registro y el envío del correo fueron exitosos, de lo contrario, False.
        """
        # Convertir el DTO en un modelo ORM Ciudadano
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
        
        # Registrar el usuario en la base de datos
        _id = self.register_repository.register_user(citizen)  # Guardar en la base de datos
        if not _id:
            return False  # Si no se pudo registrar, retornar False

        # Si el registro es exitoso, generar un código de validación
        generated_code = self.code.register_code(_id)
        
        # Si el código se genera correctamente, enviar un correo de verificación al usuario
        if generated_code:  
            self.email_sender.send_verification_email(citizen.correo, generated_code)
            return True  # Registro y correo exitoso
        return False  # Si el código no pudo generarse, retornar False

    def check_validation_code(self, id: str, code: str) -> bool:
        """
        Verifica si un código de validación es válido y no ha expirado.
        - **id**: ID del ciudadano a verificar.
        - **code**: Código de validación a verificar.
        
        Retorna None si el código no se encuentra, False si está expirado y True si es válido.
        """
        cliente = self.register_repository.check_username_exists("", id)
        expired = self.code.is_code_expired(code, cliente.id)  # Verificar si el código ha expirado
        if expired is None:
            return None  # El código no se encuentra
        if not expired:
            self.register_repository.check_validation_code(cliente.id)  # Verificar si el código es válido
            return True  # El código es válido
        return False  # El código ha expirado

    def refresh_code(self, id) -> bool:
        """
        Refresca el código de validación de un ciudadano.
        - **id**: ID del ciudadano para el cual se generará un nuevo código.
        
        Si el código se genera y el correo es enviado, retorna True.
        Si no, retorna False.
        """
        
        cliente = self.register_repository.check_username_exists("", id)
        refresh_code = self.code.refresh_code(cliente.id)  # Generar un nuevo código de validación
       

        if refresh_code is not None:  
            self.email_sender.send_verification_email(cliente.correo, refresh_code)  # Enviar correo con el nuevo código
            return True  # Código refrescado y correo enviado exitosamente

        return False  # No se pudo generar el nuevo código

    def register_bulk(self, users: List[CitizenDTO]) -> dict:
        """
        Registra múltiples usuarios en un solo proceso.
        - **users**: Lista de objetos CitizenDTO con los datos de los usuarios a registrar.
        
        Devuelve un diccionario con el estado del registro masivo:
        - **success**: Booleano que indica si al menos un registro fue exitoso.
        - **message**: Mensaje que indica el resultado del registro masivo.
        - **registered**: Lista de correos de los usuarios registrados exitosamente.
        - **failed**: Lista de errores de los usuarios que no fueron registrados.
        """
        success = []  # Lista para los correos de los usuarios registrados exitosamente
        failed = []  # Lista para los errores de los usuarios fallidos

        for dto in users:
            try:
                result = self.register(dto)  # Intentar registrar a cada usuario
                if result:
                    success.append(dto.correo)  # Si el registro es exitoso, añadir el correo a la lista de éxitos
                else:
                    failed.append({"correo": dto.correo, "error": "Usuario ya existe o inválido"})  # Si falla, añadir a la lista de errores
            except Exception as e:
                failed.append({"correo": dto.correo, "error": str(e)})  # Si ocurre una excepción, añadir a la lista de errores

        return {
            "success": len(success) > 0,  # Si al menos un usuario fue registrado exitosamente
            "message": f"{len(success)} registrados, {len(failed)} fallidos.",  # Mensaje con la cantidad de registros exitosos y fallidos
            "registered": success,  # Lista de correos de usuarios registrados
            "failed": failed  # Lista de errores de los usuarios fallidos
        }

    def get_user_by_verification(self, verification: str) -> List[CitizenDTO]:
        """
        Obtiene los usuarios según su estado de verificación.
        - **verification**: Booleano que indica si se desean obtener usuarios verificados (True) o no verificados (False).
        
        Devuelve una lista de objetos CitizenDTO con los usuarios filtrados.
        """
        ciudadanos = self.register_repository.get_user_by_verification(verification)  # Obtener usuarios por estado de verificación
        return [CitizenDTO.model_validate(ciudadano) for ciudadano in ciudadanos]  # Retornar los usuarios como objetos DTO
