from django.conf import settings
from celery import shared_task
from .utils.emails.email_sender import send_notification_email
# from .utils.machine.get_data_machine import get_client_info
# from .utils.location.get_location_info import get_location_info
import logging

logger = logging.getLogger(__name__)

@shared_task
def send_notification_email_task(user_email, device_info, location_info):
    try:
        subject = 'Novo Usuário Criado'
        message = f'Um novo usuário foi criado com o e-mail: {user_email}, {device_info}, {location_info}'
        logger.info(message)
        #send_notification_email(user_email, device_info, location_info)
    except Exception as e:
        logger.error(f"Erro ao tentar enviar o e-mail de criaçao de usuário: {str(e)}")