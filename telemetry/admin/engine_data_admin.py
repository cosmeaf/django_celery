from django.contrib import admin
from security.models import CustomUser
from telemetry.models.engine_data_model import EngineData

@admin.register(EngineData)
class EngineDataAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'temperature_engine_coolant', 'oil_pressure', 'engine_oil_temperature')