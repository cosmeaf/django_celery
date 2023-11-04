# customManager/forms.py
from django import forms
from customManager.models.address_model import Address
from security.models import CustomUser


class AddressForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=CustomUser.objects.all(),
        to_field_name="email",
        label="User",
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )

    class Meta:
        model = Address
        fields = ['cep', 'logradouro', 'complemento', 'bairro', 'localidade', 'uf', 'user']

    def clean(self):
        cleaned_data = super().clean()
        user = cleaned_data.get('user')
        cep = cleaned_data.get('cep')
        if Address.objects.filter(user=user, cep=cep).exists():
            raise forms.ValidationError("Endereço com este CEP já cadastrado para este usuário.")
    
    def __init__(self, *args, **kwargs):
        current_user = kwargs.pop('current_user', None)
        super(AddressForm, self).__init__(*args, **kwargs)
        
        if current_user:
            self.fields['user'].initial = current_user
            self.fields['user'].widget = forms.HiddenInput()

