from django.contrib import admin
from security.models import CustomUser
from telemetry.models.cooling_system_data_model import CoolingSystemData

@admin.register(CoolingSystemData)
class CoolingSystemDataAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'coolant_temperature', 'coolant_pressure', 'coolant_flow')