# Importa 'APIRouter', 'Depends' y 'HTTPException' desde FastAPI para crear rutas y gestionar dependencias y errores.
from fastapi import APIRouter, Depends, HTTPException

# Importa 'List' para especificar que la respuesta será una lista de objetos de tipo 'SecurityFrontDTO'.
from typing import List  # <-- Importación faltante

# Importa la implementación del servicio para frentes de seguridad.
from app.security_fronts.infrastructure.service.security_front_service_impl import SecurityFrontServiceImpl

# Importa el DTO (Data Transfer Object) que representa los datos de un frente de seguridad.
from app.security_fronts.application.dto.security_front_dto import SecurityFrontDTO

# Define una función para crear el router de FastAPI que manejará las rutas de los frentes de seguridad.
def create_router(get_security_front_service):
    # Crea un objeto 'router' de FastAPI para manejar las rutas.
    router = APIRouter()

    # Ruta para registrar un nuevo frente de seguridad.
    @router.post("/security-fronts", response_model=SecurityFrontDTO)
    def register_security_front(dto: SecurityFrontDTO, service: SecurityFrontServiceImpl = Depends(get_security_front_service)):
        # Llama al servicio para registrar el frente de seguridad. Si tiene éxito, retorna el DTO.
        if service.register(dto):
            return dto
        # Si no se puede registrar el frente, lanza una excepción HTTP 400 (Bad Request).
        raise HTTPException(status_code=400, detail="No se pudo registrar el frente de seguridad")

    # Ruta para obtener todos los frentes de seguridad.
    @router.get("/security-fronts", response_model=List[SecurityFrontDTO])
    def get_security_fronts(service: SecurityFrontServiceImpl = Depends(get_security_front_service)):
        # Llama al servicio para obtener todos los frentes de seguridad.
        return service.get_all()

    # Ruta para obtener un frente de seguridad por su ID.
    @router.get("/security-fronts/{frente_id}", response_model=SecurityFrontDTO)
    def get_security_front_by_id(frente_id: int, service: SecurityFrontServiceImpl = Depends(get_security_front_service)):
        # Llama al servicio para obtener el frente por su ID.
        frente = service.get_by_id(frente_id)
        if not frente:
            # Si no se encuentra el frente, lanza una excepción HTTP 404 (Not Found).
            raise HTTPException(status_code=404, detail="Frente de seguridad no encontrado")
        # Si se encuentra el frente, lo retorna como respuesta.
        return frente

    # Ruta para actualizar un frente de seguridad por su ID.
    @router.put("/security-fronts/{frente_id}", response_model=SecurityFrontDTO)
    def update_security_front(frente_id: int, dto: SecurityFrontDTO, service: SecurityFrontServiceImpl = Depends(get_security_front_service)):
        # Llama al servicio para actualizar el frente con el ID y el DTO proporcionado.
        if service.update(frente_id, dto):
            return dto
        # Si no se puede actualizar el frente, lanza una excepción HTTP 400 (Bad Request).
        raise HTTPException(status_code=400, detail="No se pudo actualizar el frente de seguridad")

    # Ruta para eliminar un frente de seguridad por su ID.
    @router.delete("/security-fronts/{frente_id}", response_model=bool)
    def delete_security_front(frente_id: int, service: SecurityFrontServiceImpl = Depends(get_security_front_service)):
        # Llama al servicio para eliminar el frente de seguridad con el ID proporcionado.
        success = service.delete(frente_id)
        if not success:
            # Si no se puede eliminar el frente, lanza una excepción HTTP 400 (Bad Request).
            raise HTTPException(status_code=400, detail="No se pudo eliminar el frente de seguridad")
        # Retorna un valor booleano indicando si la eliminación fue exitosa.
        return success  # <-- Retorno faltante

    # Retorna el router que contiene todas las rutas definidas.
    return router
