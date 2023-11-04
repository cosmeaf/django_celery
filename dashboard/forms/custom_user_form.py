from django import forms
from django.forms.models import inlineformset_factory
from django.db import transaction
from security.models import CustomUser
from customManager.models.address_model import Address
from customManager.models.vehicle_model import Vehicle
from customManager.models.appointment_model import Appointment
from django.utils.crypto import get_random_string
from dashboard.tasks import send_notification_email_task
from dashboard.utils.machine.get_data_machine import get_client_info
from dashboard.utils.location.get_location_info import get_location_info

# Define formsets
AddressFormSet = inlineformset_factory(
    CustomUser, Address, fields=('cep', 'logradouro', 'complemento', 'bairro', 'localidade', 'uf'), extra=1, can_delete=True
)
VehicleFormSet = inlineformset_factory(
    CustomUser, Vehicle, fields=('brand', 'model', 'fuel', 'year', 'odometer', 'plate', 'vin'), extra=1, can_delete=True
)
AppointmentFormSet = inlineformset_factory(
    CustomUser, Appointment, fields=('address', 'vehicle', 'service', 'hour', 'day', 'protocol', 'employee', 'cancellation_reason'), extra=1, can_delete=True
)

class CustomUserForm(forms.ModelForm):
    email = forms.EmailField(
        label="E-mail",
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        error_messages={
            'required': 'Por favor, insira um e-mail.',
            'invalid': 'Por favor, insira um e-mail válido.',
        }
    )

    first_name = forms.CharField(
        label="Nome",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        error_messages={
            'required': 'Por favor, insira o primeiro nome.',
        }
    )

    last_name = forms.CharField(
        label="Sobrenome",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        error_messages={
            'required': 'Por favor, insira o sobrenome.',
        }
    )


    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CustomUserForm, self).__init__(*args, **kwargs)
        self.fields['password'].required = False  # A senha não é obrigatória no formulário
        self.address_formset = AddressFormSet(instance=self.instance)
        self.vehicle_formset = VehicleFormSet(instance=self.instance)
        self.appointment_formset = AppointmentFormSet(instance=self.instance)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Esse e-mail já está cadastrado.")
        return email

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        if not self.cleaned_data['password']: 
            password = get_random_string(length=12)
            user.set_password(password)
        elif self.cleaned_data['password']: 
            user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()
            self.address_formset.instance = user
            self.vehicle_formset.instance = user
            self.appointment_formset.instance = user
            
            self.address_formset.save()
            self.vehicle_formset.save()
            self.appointment_formset.save()

            # Recupera informações do cliente e envia e-mail
            if self.request:
                ip_address = self.request.META.get('REMOTE_ADDR')
                machine_info = get_client_info(self.request)
                location_info = get_location_info(ip_address)
                send_notification_email_task.delay(user.email, machine_info, location_info)

        return user