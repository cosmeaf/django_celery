from django.contrib import admin
from security.models import CustomUser
from telemetry.models.diagnostics_data_model import DiagnosticsData

@admin.register(DiagnosticsData)
class DiagnosticsDataAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'code', 'message', 'history')