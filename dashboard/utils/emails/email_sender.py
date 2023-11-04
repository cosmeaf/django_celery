from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def send_notification_email(email, device_info, location_info):
    subject = 'Conta Criada no Sistema XPTO'
    
    try:
        message = (
            f"Olá,\n\n"
            f"Uma nova conta foi criada com o e-mail: {email} no Sistema XPTO.\n\n"
            f"Informações da máquina:\n"
            f"Browser: {device_info['browser']}\n"
            f"Versão do Browser: {device_info.get('browser_version', 'Não informado')}\n"
            f"Dispositivo: {device_info['device']}\n"
            f"Sistema Operacional: {device_info['os_name']}\n"
            f"Versão do Sistema Operacional: {device_info['os_version']}\n\n"
            f"Informações de localização:\n"
            f"IP: {location_info['ip']}\n"
            f"ISP: {location_info['isp']}\n"
            f"País: {location_info['country']}\n"
            f"Estado: {location_info['state']}\n"
            f"Cidade: {location_info['city']}\n"
            f"Código Postal: {location_info['zipcode']}\n"
        )
        send_mail(subject, message, settings.EMAIL_HOST_USER, [email], fail_silently=False)

        logger.info("E-mail enviado com sucesso.")
        return True
    except BadHeaderError:  
        logger.error("Erro nos headers do e-mail.")
        return False
    except Exception as e:
        logger.error(f"Erro ao enviar e-mail: {e}")
        return False
