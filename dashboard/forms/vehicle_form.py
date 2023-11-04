from django import forms
from security.models import CustomUser
from customManager.models.vehicle_model import Vehicle

class VehicleForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=CustomUser.objects.all(),
        to_field_name="email",
        label="User",
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )

    class Meta:
        model = Vehicle
        fields = ['brand', 'model', 'fuel', 'year', 'odometer', 'plate', 'user']

    def clean(self):
        cleaned_data = super().clean()
        user = cleaned_data.get('user')
        plate = cleaned_data.get('plate')
        if Vehicle.objects.filter(user=user, plate=plate).exists():
            raise forms.ValidationError("Veículo já cadastrado para este usuário.")
            
    def __init__(self, *args, **kwargs):
        current_user = kwargs.pop('current_user', None)
        super(VehicleForm, self).__init__(*args, **kwargs)
        
        if current_user:
            self.fields['user'].initial = current_user
            self.fields['user'].widget = forms.HiddenInput()
