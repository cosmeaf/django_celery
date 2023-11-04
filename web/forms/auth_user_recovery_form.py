from django import forms
from security.models import CustomUser 
from security.utils.machine.get_data_machine import get_client_info
from security.utils.location.get_location_info import get_location_info
from security.utils.otp_handler import create_or_update_recovery_data

class AuthUserRecoveryForm(forms.Form):
    email = forms.EmailField(label='E-mail', max_length=254)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = CustomUser.objects.filter(email=email).first()

        if not user:
            raise forms.ValidationError('E-mail não encontrado')

        ip_address = self.initial['request'].META.get('REMOTE_ADDR')
        device_info = get_client_info(self.initial['request'])
        location_info = get_location_info(ip_address)
        recovery_data = create_or_update_recovery_data(user, ip_address, device_info)

        # Substitua isso pelo código relevante para o envio do email ou ação desejada no frontend
        # send_email_otp_task.delay(email, recovery_data.otp, device_info, location_info)

        return email
