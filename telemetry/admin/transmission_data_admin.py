from django.contrib import admin
from security.models import CustomUser
from telemetry.models.transmission_data_model import TransmissionData


@admin.register(TransmissionData)
class TransmissionDataAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'transmission_fluid_temperature', 'transmission_fluid_pressure', 'transmission_speed')