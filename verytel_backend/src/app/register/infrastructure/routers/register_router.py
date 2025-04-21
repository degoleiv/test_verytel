
from fastapi import APIRouter, Depends

from app.register.application.services.register_service import RegisterService
from app.register.application.dto.citizen_dto import CitizenDTO

from fastapi import HTTPException, status
def create_router(get_register_service):
    app = APIRouter()


    @app.post("/register")
    def register_user(dto: CitizenDTO, service: RegisterService = Depends(get_register_service)):
        register = service.register(dto)
        if register:
            return {"message": "Usuario Registrado con éxito"}
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Usuario encontrado o no se ha podido verificar"
        )


    @app.get("/validation")
    def validate_user(id: str, code: str, service: RegisterService = Depends(get_register_service)):
        validation = service.check_validation_code(id, code)

        if validation is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Código no encontrado"
            )
        elif validation is False:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Código ya fue usado anteriormente"
            )

        return {"message": "Usuario verificado con éxito"}
    return app