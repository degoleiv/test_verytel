
class EmailRespository ():
    @staticmethod
    def get_verification_email_content(code: str):
        subject = "Código de Verificación"
        content = f"Tu código de verificación para el Frente de Seguridad es: {code}"
        return subject, content