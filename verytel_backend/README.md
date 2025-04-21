
# Documentación del Backend

Este es el backend del proyecto **Prueba tecnica Verytel** que proporciona funcionalidades de registro de usuarios, validación de códigos de verificación, y manejo de frentes de seguridad.

## Arquitectura

El sistema sigue una arquitectura basada en **Microservicios** y **Arquitectura Hexagonal** para asegurar la escalabilidad, la separación de preocupaciones y la facilidad de mantenimiento.

### Componentes principales

1. **App**: El objeto principal de la aplicación FastAPI.
2. **Servicios**: Encapsulan la lógica de negocio y se comunican con los repositorios para realizar las operaciones necesarias en la base de datos.
3. **Repositorios**: Gestionan las operaciones de base de datos a través de SQLAlchemy y proporcionan una capa de abstracción sobre las consultas a la base de datos.
4. **Factories**: Inicializan y gestionan las conexiones a la base de datos y al servicio de correo electrónico.

## Endpoints

### 1. `/signin/register`

**Método**: `POST`

Este endpoint permite registrar un nuevo usuario. Los datos del usuario se envían en el cuerpo de la solicitud, y el sistema genera un código de verificación, que luego se envía al correo del usuario.


### 2. `signin/validation`

**Método**: `GET`

Este endpoint permite verificar el código de verificación enviado al correo del usuario. El código se pasa como un parámetro en la URL.


## Documentación del Backend

### 3. `security/security-fronts`
**Método**: `GET`  
**Descripción**:  
Este endpoint devuelve la lista de todos los frentes de seguridad registrados en el sistema.

**Respuesta**:  
- `200 OK`: Retorna una lista de frentes de seguridad.

### 4. `security/security-fronts/{id_frente}`
**Método**: `GET`  
**Descripción**:  
Este endpoint devuelve la información detallada de un frente de seguridad específico, identificado por su `id_frente`.

**Parámetros**:
- `id_frente`: ID del frente de seguridad a obtener.

**Respuesta**:
- `200 OK`: Retorna los detalles del frente de seguridad.
- `404 Not Found`: Si el frente de seguridad no se encuentra en el sistema.

### 5. `security/security-fronts`
**Método**: `POST`  
**Descripción**:  
Este endpoint se utiliza para crear un nuevo frente de seguridad.

**Cuerpo de la solicitud**:
- `nombre`: Nombre del frente de seguridad.
- `descripcion`: Descripción del frente de seguridad.

**Respuesta**:
- `201 Created`: Si el frente de seguridad se crea exitosamente.
- `400 Bad Request`: Si la solicitud está incompleta o mal formada.

### 6. `security/security-fronts/{id_frente}`
**Método**: `PUT`  
**Descripción**:  
Este endpoint actualiza la información de un frente de seguridad existente.

**Parámetros**:
- `id_frente`: ID del frente de seguridad a actualizar.

**Cuerpo de la solicitud**:
- `nombre`: Nombre actualizado del frente de seguridad.
- `descripcion`: Descripción actualizada del frente de seguridad.

**Respuesta**:
- `200 OK`: Si el frente de seguridad se actualiza exitosamente.
- `404 Not Found`: Si no se encuentra el frente de seguridad a actualizar.
- `400 Bad Request`: Si la solicitud está incompleta o mal formada.

### 7. `security/security-fronts/{id_frente}`
**Método**: `DELETE`  
**Descripción**:  
Este endpoint elimina un frente de seguridad existente.

**Parámetros**:
- `id_frente`: ID del frente de seguridad a eliminar.

**Respuesta**:
- `200 OK`: Si el frente de seguridad se elimina exitosamente.
- `404 Not Found`: Si no se encuentra el frente de seguridad a eliminar.



## Estructura del Proyecto

```plaintext
src/
│
├── app/
│   ├── config/
│   │   ├── database/
│   │   └── email/
│   ├── security_fronts/
│   ├── register/
│   └── main.py
├── 
│    .env
├── requirements.txt
```

## Dependencias

### Backend

- `FastAPI`: Framework de alto rendimiento para construir APIs.
- `SQLAlchemy`: ORM para interactuar con la base de datos.
- `Pydantic`: Para la validación de datos.
- `psycopg2`: Conector para PostgreSQL.
- `smtplib`: Para enviar correos electrónicos utilizando SMTP.
- `python-dotenv`: Para gestionar variables de entorno.

### Base de Datos

Se utiliza **PostgreSQL** como base de datos relacional para almacenar la información de los usuarios y los frentes de seguridad **Esta se encuentra en el servicio Always Data**.



## Flujo de Registro de Usuario

1. El usuario envía una solicitud de registro con los datos necesarios.
2. El sistema genera un código de verificación único.
3. Se envía el código de verificación al correo electrónico del usuario.
4. El usuario ingresa el código recibido en el endpoint de verificación.
5. Si el código es válido, el sistema marca al usuario como verificado.

## Flujo de Envío de Correo

1. Cuando se crea un nuevo usuario, se envía un correo con el código de verificación utilizando el servicio de correo configurado.
2. La clase `EmailConnectionFactory` gestiona las conexiones SMTP para enviar correos utilizando **Gmail**.

## Variables de Entorno

Las siguientes variables deben ser configuradas en el archivo `.env` para el funcionamiento adecuado de la aplicación:

```plaintext
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=465
SMTP_USERNAME=catproyect1@gmail.com
SMTP_PASSWORD=dwqi nxda wrtb gzyt
DATABASE_URL=postgresql://usuario:contraseña@localhost/dbname
```

## Consideraciones de Seguridad

- El código de verificación debe ser único y tener una fecha de expiración.
- Las contraseñas de los usuarios deben almacenarse de manera segura utilizando un hash.


## Despliegue

Para desplegar la aplicación, simplemente configura las variables de entorno y ejecuta la aplicación utilizando **Docker** o de forma local con el comando:

```bash
$ uvicorn src.app.main:application --reload
```

