from django.contrib import admin
from security.models import CustomUser
from telemetry.models.electrical_system_data_model import ElectricalSystemData

@admin.register(ElectricalSystemData)
class ElectricalSystemDataAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'battery_voltage', 'battery_current', 'battery_charge', 'battery_state_of_charge')