from django.contrib import admin
from security.models import CustomUser
from telemetry.models.fuel_data_model import FuelData


@admin.register(FuelData)
class FuelDataAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'fuel_consumption', 'average_speed', 'fuel_efficiency')