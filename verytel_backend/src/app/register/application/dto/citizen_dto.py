from pydantic import (
    BaseModel,
    EmailStr,
)  
from typing import (
    Optional,
)  
from datetime import date 


# Definimos un DTO (Data Transfer Object) para representar un ciudadano.
class CitizenDTO(BaseModel):
    nombres: str  # Campo obligatorio para el primer nombre del ciudadano.
    apellidos: str  # Campo obligatorio para los apellidos del ciudadano.
    identificacion: str  # Campo obligatorio para la identificación del ciudadano (por ejemplo, número de cédula o pasaporte).
    correo: EmailStr  # Campo obligatorio para el correo electrónico del ciudadano, validado como una dirección de correo.
    celular: str  # Campo obligatorio para el número de celular del ciudadano.
    barrio: str  # Campo obligatorio para el barrio donde reside el ciudadano.
    direccion: str  # Campo obligatorio para la dirección del ciudadano.
    frente_seguridad_id: int  # Campo obligatorio para el ID del frente de seguridad al que pertenece el ciudadano.
    tipo_documento: str  # Campo obligatorio para especificar el tipo de documento del ciudadano (por ejemplo, cédula, pasaporte).
    fecha_nacimiento: date  # Campo obligatorio para la fecha de nacimiento del ciudadano, con el tipo 'date' de Python.
    sexo: str  # Campo obligatorio para especificar el sexo del ciudadano.
    antecedentes: (
        bool  # Campo obligatorio que indica si el ciudadano tiene antecedentes o no.
    )
    justificacion_antecedentes: Optional[str] = (
        None  # Campo opcional para justificar los antecedentes, si los tiene. Puede ser nulo.
    )
    foto: Optional[bytes] = (
        None  # Campo opcional para la foto del ciudadano. Se almacena como datos binarios y puede ser nulo.
    )
    usuario_verificado: Optional[bool] = (None
    )

    # Configuración adicional de Pydantic, indicamos que se deben aceptar atributos al crear la instancia desde el diccionario.
    model_config = {
        "from_attributes": True  # Permite que los atributos del objeto sean pasados directamente al crear el DTO.
    }
