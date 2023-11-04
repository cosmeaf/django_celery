from django.db import models
from telemetry.models.base_model import Base
from customManager.models.vehicle_model import Vehicle


class FuelData(Base):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='fuel_data_related')
    fuel_consumption = models.FloatField('Consumo de Combustível')
    average_speed = models.FloatField('Velocidade Média')
    fuel_efficiency = models.FloatField('Eficiência de Combustível')
    fuel_temperature = models.FloatField('Temperatura do Combustível')
    fuel_pressure = models.FloatField('Pressão do Combustível')

    class Meta:
        verbose_name = "Dado de Combustível"
        verbose_name_plural = "Dados de Combustível"
        ordering = ['-deleted_at', '-updated_at', 'vehicle']
        indexes = [
            models.Index(fields=['fuel_consumption']),
        ]

    def __str__(self):
        return f"{self.vehicle.plate} - {self.fuel_consumption}"
