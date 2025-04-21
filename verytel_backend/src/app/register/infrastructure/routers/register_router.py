from fastapi import APIRouter, Depends

from app.register.application.services.register_service import RegisterService
from app.register.application.dto.citizen_dto import CitizenDTO
from typing import List
from fastapi import HTTPException, status

# Definición de la función para crear las rutas del router
def create_router(get_register_service):
    app = APIRouter()

    # Ruta para registrar un solo usuario
    @app.post("/register")
    def register_user(dto: CitizenDTO, service: RegisterService = Depends(get_register_service)):
        """
        Ruta para registrar un único usuario.
        - **dto**: Un objeto de tipo CitizenDTO que contiene los datos del ciudadano a registrar.
        - **service**: Dependencia de RegisterService que maneja la lógica de registro.
        
        Si el registro es exitoso, devuelve un mensaje de éxito.
        Si no, lanza una excepción HTTP 409 en caso de conflicto (usuario ya registrado o no verificado).
        """
        register = service.register(dto)  # Llama al servicio para registrar al usuario
        if register:
            return {"message": "Usuario Registrado con éxito"}
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Usuario encontrado o no se ha podido verificar"
        )
        
    # Ruta para registrar múltiples usuarios a la vez
    @app.post("/register/bulk")
    def register_users_bulk(dtos: List[CitizenDTO], service: RegisterService = Depends(get_register_service)):
        """
        Ruta para registrar múltiples usuarios de manera masiva.
        - **dtos**: Lista de objetos CitizenDTO con los datos de los usuarios a registrar.
        
        Llama al servicio para realizar el registro masivo de usuarios.
        Si no es exitoso, lanza una excepción HTTP 207 para mostrar múltiples estados.
        Si es exitoso, devuelve un mensaje con el resultado.
        """
        results = service.register_bulk(dtos)  # Llama al servicio para el registro masivo

        if not results["success"]:
            raise HTTPException(
                status_code=status.HTTP_207_MULTI_STATUS,
                detail=results["message"]
            )
        
        return {"message": "Registro masivo completado", "data": results}

    # Ruta para obtener usuarios según su estado de verificación
    @app.get("/users_verification")
    def users_verification(
        verification: str, 
        service: RegisterService = Depends(get_register_service)
    ):
        """
        Ruta para obtener usuarios que coinciden con el estado de verificación.
        - **verification**: Booleano que indica si se desean obtener usuarios verificados (True) o no verificados (False).
        
        Llama al servicio para obtener los usuarios que tienen el estado de verificación indicado.
        Retorna una lista de usuarios.
        """
        users = service.get_user_by_verification(verification)
        return users

    # Ruta para validar un código de verificación
    @app.get("/validation")
    def validate_user(id: str, code: str, service: RegisterService = Depends(get_register_service)):
        """
        Ruta para verificar un código de validación para un usuario.
        - **id**: ID del usuario a verificar.
        - **code**: Código de validación a verificar.
        
        Si el código no existe o está expirado, lanza una excepción HTTP 404 o HTTP 409.
        Si es válido, devuelve un mensaje de éxito.
        """
        validation = service.check_validation_code(id, code)  # Llama al servicio para verificar el código

        if validation is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Código no encontrado"
            )
        elif validation is False:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Código ya fue usado anteriormente o esta expirado"
            )

        return {"message": "Usuario verificado con éxito"}

    # Ruta para refrescar un código de validación
    @app.get("/refresh")
    def refresh_code(id: str, service: RegisterService = Depends(get_register_service)):
        """
        Ruta para generar un nuevo código de validación para un usuario.
        - **id**: ID del usuario para el cual se generará un nuevo código.
        
        Si el código se genera con éxito, devuelve un mensaje de éxito.
        Si no, lanza una excepción HTTP 409 si no se pudo generar el código.
        """
        
        
        
        refresh = service.refresh_code(id)  # Llama al servicio para refrescar el código de validación
        if refresh:
             return {"message": "codigo nuevo generado con exito"}

        raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="No se pudo generar un nuevo codigo consulte con el administrador"
            )
    
    # Devuelve el objeto app con las rutas definidas
    return app
