from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.database.db_connection_factory import DatabaseConnectionFactory
from app.config.email.email_connection_factory import EmailConnectionFactory

application = FastAPI()

application.add_middleware(
  CORSMiddleware,
  allow_origins=["http://localhost", "http://localhost:5173"],  
  allow_credentials=True,
  allow_methods=["GET", "POST","PUT","DELETE"], 
  allow_headers=["Content-Type","Set-Cookie","Authorization"], 
)


def migrate_register():
    from app.security_fronts.domain.entities.security_front import FrenteSeguridad
    from app.register.domain.entities.citizen import Ciudadano
    
    from app.register.domain.entities.validation_codes import ValidationCode
    from app.config.database.base import Base
    from app.config.database.db_connection_factory import DatabaseConnectionFactory

    try:
        print("⏳ Ejecutando migración de entidades...")
        engine = DatabaseConnectionFactory.get_engine()
        Base.metadata.create_all(bind=engine)
        print("✅ Migración completada con éxito.")
    except Exception as e:
        print(f"❌ Error al ejecutar migración: {e}")
    

@application.on_event("startup")
def startup():
    print("Initializing connection pool")
    DatabaseConnectionFactory.initialize_connection_pool()
    EmailConnectionFactory.initialize_connection_pool()
    migrate_register()



@application.on_event("shutdown")
def shutdown():
    print("Closing all connections")
    DatabaseConnectionFactory.close_all_connections()
    EmailConnectionFactory.close_all_connections()
    




# Inyeccion de dependencia de componente de registro 
from app.register.infrastructure.routers.register_router import create_router as register_router
def get_register_service():
    from app.register.infrastructure.repositories.register_repository_impl import RegisterRepositoryImpl
    
    from app.shared.infrastructure.service.email_service_impl import EmailServiceImpl
    
    from app.register.infrastructure.service.register_service_impl import RegisterServiceImpl
    
    from app.register.infrastructure.repositories.validationcode_repository_impl import ValidationCodeRepositoryImpl
    
    
    db = DatabaseConnectionFactory.get_session()
    repo = RegisterRepositoryImpl(db)
    code = ValidationCodeRepositoryImpl(db)
    email = EmailServiceImpl()
    
    service = RegisterServiceImpl(repo, email, code)
    try:
         yield service
    finally:
        db.close()
application.include_router(register_router(get_register_service), prefix="/signin", tags=["signin"]) 



from app.security_fronts.infrastructure.routers.security_front_router import create_router as security_router
from app.security_fronts.infrastructure.repositories.security_front_repository_impl import FrenteSeguridadRepositoryImpl
from app.security_fronts.infrastructure.service.security_front_service_impl import SecurityFrontServiceImpl
from app.security_fronts.application.dto.security_front_dto import SecurityFrontDTO




# Inyeccion de dependencia de componente de frente de seguridad 

def security_dependency_injection():
    db = DatabaseConnectionFactory.get_session()
    try:
        repo = FrenteSeguridadRepositoryImpl(db)
        service = SecurityFrontServiceImpl(repo)
        yield service
    finally:
        db.close()

def get_security_service():
    return next(security_dependency_injection())


application.include_router(security_router(security_dependency_injection), prefix="/security", tags=["security"])
@application.on_event("startup")
# ---- Carga de datos de prueba ----
def security_insert_example():
    
    # service =  security_dependency_injection()
    frentes_prueba = [
        SecurityFrontDTO(nombre="Frente de Seguridad Comuna 13", descripcion="Ubicado en Medellín, zona occidental."),
        SecurityFrontDTO(nombre="Frente de Seguridad Chapinero", descripcion="Zona comercial y residencial de Bogotá."),
        SecurityFrontDTO(nombre="Frente de Seguridad Ciudad Jardín", descripcion="Sector sur de Cali."),
        SecurityFrontDTO(nombre="Frente de Seguridad El Prado", descripcion="Barranquilla, tradicional y residencial."),
        SecurityFrontDTO(nombre="Frente de Seguridad La Candelaria", descripcion="Centro histórico de Bogotá.")
    ]
    engine = DatabaseConnectionFactory.get_session()
 
 
    repo = FrenteSeguridadRepositoryImpl(engine)
    service = SecurityFrontServiceImpl(repo)
    for frente in frentes_prueba:
        try:
           
            service.register(frente)
          
        except Exception as e:
            print(f"Error al registrar {frente.nombre}: {e}")
