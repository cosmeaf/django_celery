
from django.db import models
from telemetry.models.base_model import Base
from customManager.models.vehicle_model import Vehicle

class BrakeData(Base):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='brake_data_related')
    brake_temperature = models.FloatField('Temperatura do Freio')
    brake_pad_wear = models.FloatField('Desgaste da Pastilha de Freio')
    brake_disc_wear = models.FloatField('Desgaste do Disco de Freio')
    brake_fluid_pressure = models.FloatField('Pressão do Fluido de Freio')

    class Meta:
        verbose_name = "Dado de Freio"
        verbose_name_plural = "Dados de Freio"
        ordering = ['-deleted_at', '-updated_at', 'vehicle']
        indexes = [
            models.Index(fields=['brake_temperature']),
        ]

    def __str__(self):
        return f"{self.vehicle.plate} - {self.brake_temperature}"
