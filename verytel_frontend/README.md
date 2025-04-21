
# Frontend - Aplicación de Verificación de Usuario

Este es el frontend de la aplicación web para la verificación de usuarios. Está construido con **React** y **React Router**.

# Documentación del Formulario de Registro

## Descripción
Este componente de formulario permite a los usuarios registrar información personal, incluyendo su nombre, apellidos, tipo de documento, identificación, correo, celular, barrio, dirección, fecha de nacimiento, y otros campos relevantes como el sexo, antecedentes y el frente de seguridad asociado.

El formulario valida la entrada de datos utilizando un hook personalizado y envía la información mediante otro hook para su posterior procesamiento. 

### Componentes del formulario:
- Primer Nombre
- Primer Apellido
- Tipo de Documento
- Número de Identificación
- Correo Electrónico
- Número de Celular
- Barrio
- Dirección Exacta
- Fecha de Nacimiento
- Frente de Seguridad Asociado
- Sexo
- ¿Tiene Antecedentes?
- Justificación de Antecedentes (si aplica)

## Requisitos

- Node.js (versión 14 o superior)
- npm o yarn

## Instalación

1. Clona el repositorio:
   ```bash
   git clone 
   cd frontend-verificacion
   ```

2. Instala las dependencias:
   ```bash
   npm install
   ```

   O si usas **yarn**:
   ```bash
   yarn install
   ```

3. Inicia el servidor de desarrollo:
   ```bash
   npm start
   ```

   El servidor se ejecutará en `http://localhost:3000`.

## Estructura del Proyecto
el Proyecto utiliza la metodologia de Screaming arquitecture, esto quiere decir que cada funcionalidad del sistema esta dividida por componente con su respectivas carpetas 
- `src/utils`: Contiene los archivos usables para cualquier carpeta .
- `src/hooks/`: Archivos para manejar la lógica y las api .
- `src/component/`: Componentes y lógica 
- `src/assets/`: Archivos de estilo (CSS) y otros recursos estáticos.

## Rutas

### 1. **/**

Página principal donde el usuario puede enviar un código de verificación.

### 2. **/validation**

Página donde el usuario será redirigido después de un envío exitoso para continuar con la validación.

## Funcionalidad

1. **Formulario de envío**:
   El formulario captura un código de verificación y lo envía al backend para ser validado.
   
   Si el código es válido, el usuario es redirigido a la página de validación. Si hay un error, se muestra un mensaje de error usando **react-toastify**.

2. **Navegación protegida**:
   Se utiliza **React Router** para manejar las rutas. La página de validación está protegida y solo accesible después de una validación exitosa.

## Variables de Entorno

Configura las siguientes variables de entorno en tu archivo `.env`:

- `REACT_APP_API_URL`: La URL del backend donde se realizan las solicitudes (por ejemplo: `http://127.0.0.1:8000`).
