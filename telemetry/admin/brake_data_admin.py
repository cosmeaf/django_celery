from django.contrib import admin
from security.models import CustomUser
from telemetry.models.brake_data_model import BrakeData

@admin.register(BrakeData)
class BrakeDataAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'brake_temperature', 'brake_pad_wear', 'brake_disc_wear')