from django.db import models
from telemetry.models.base_model import Base
from customManager.models.vehicle_model import Vehicle

class CoolingSystemData(Base):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='cooling_system_data_related')
    coolant_temperature = models.FloatField('Temperatura do Refrigerante')
    coolant_pressure = models.FloatField('Pressão do Refrigerante')
    coolant_flow = models.FloatField('Fluxo do Refrigerante')

    class Meta:
        verbose_name = "Dado do Sistema de Resfriamento"
        verbose_name_plural = "Dados do Sistema de Resfriamento"
        ordering = ['-deleted_at', '-updated_at', 'vehicle']
        indexes = [
            models.Index(fields=['coolant_temperature']),
        ]


    def __str__(self):
        return f"{self.vehicle.plate} - {self.coolant_temperature}°C"
