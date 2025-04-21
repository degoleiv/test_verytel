
# Define una clase llamada 'EmailRespository'.
# Esta clase contiene métodos relacionados con la generación del contenido de correos electrónicos.
class EmailRespository():
    
    # Define un método estático que no requiere una instancia de la clase para ser llamado.
    # Recibe como parámetro un código de verificación (code) y retorna el asunto y contenido del correo.
    @staticmethod
    def get_verification_email_content(code: str):
        # Asunto del correo electrónico.
        subject = "Código de Verificación"

        # Cuerpo del mensaje, incluyendo dinámicamente el código de verificación proporcionado.
        content = f"Tu código de verificación para el Frente de Seguridad es: {code}"

        # Retorna el asunto y el contenido como una tupla.
        return subject, content
