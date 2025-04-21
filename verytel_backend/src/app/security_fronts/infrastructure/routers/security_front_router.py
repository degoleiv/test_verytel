from fastapi import APIRouter, Depends, HTTPException
from typing import List  # <-- Importación faltante

from app.security_fronts.infrastructure.service.security_front_service_impl import SecurityFrontServiceImpl
from app.security_fronts.application.dto.security_front_dto import SecurityFrontDTO

def create_router(get_security_front_service):
    router = APIRouter()

    # Ruta para registrar un nuevo frente de seguridad
    @router.post("/security-fronts", response_model=SecurityFrontDTO)
    def register_security_front(dto: SecurityFrontDTO, service: SecurityFrontServiceImpl = Depends(get_security_front_service)):
        if service.register(dto):
            return dto
        raise HTTPException(status_code=400, detail="No se pudo registrar el frente de seguridad")

    # Ruta para obtener todos los frentes de seguridad
    @router.get("/security-fronts", response_model=List[SecurityFrontDTO])
    def get_security_fronts(service: SecurityFrontServiceImpl = Depends(get_security_front_service)):
        return service.get_all()

    # Ruta para obtener un frente de seguridad por ID
    @router.get("/security-fronts/{frente_id}", response_model=SecurityFrontDTO)
    def get_security_front_by_id(frente_id: int, service: SecurityFrontServiceImpl = Depends(get_security_front_service)):
        frente = service.get_by_id(frente_id)
        if not frente:
            raise HTTPException(status_code=404, detail="Frente de seguridad no encontrado")
        return frente

    # Ruta para actualizar un frente de seguridad
    @router.put("/security-fronts/{frente_id}", response_model=SecurityFrontDTO)
    def update_security_front(frente_id: int, dto: SecurityFrontDTO, service: SecurityFrontServiceImpl = Depends(get_security_front_service)):
        if service.update(frente_id, dto):
            return dto
        raise HTTPException(status_code=400, detail="No se pudo actualizar el frente de seguridad")

    # Ruta para eliminar un frente de seguridad
    @router.delete("/security-fronts/{frente_id}", response_model=bool)
    def delete_security_front(frente_id: int, service: SecurityFrontServiceImpl = Depends(get_security_front_service)):
        success = service.delete(frente_id)
        if not success:
            raise HTTPException(status_code=400, detail="No se pudo eliminar el frente de seguridad")
        return success  # <-- Retorno faltante

    return router
