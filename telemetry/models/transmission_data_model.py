
from django.db import models
from telemetry.models.base_model import Base
from customManager.models.vehicle_model import Vehicle


class TransmissionData(Base):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='transmission_data_related')
    transmission_fluid_temperature = models.FloatField('Temperatura do Fluido da Transmissão')
    transmission_fluid_pressure = models.FloatField('Pressão do Fluido da Transmissão')
    transmission_speed = models.IntegerField('Velocidade da Transmissão')
    gear_position = models.CharField('Posição da Engrenagem', max_length=20)
    transmission_ratio = models.FloatField('Relação da Transmissão')
    transmission_torque = models.FloatField('Torque da Transmissão')

    class Meta:
        verbose_name = "Dado de Transmissão"
        verbose_name_plural = "Dados de Transmissão"
        ordering = ['-deleted_at', '-updated_at', 'vehicle']
        unique_together = ('vehicle', 'gear_position')
        indexes = [
            models.Index(fields=['gear_position']),
        ]


    def __str__(self):
        return f"{self.vehicle.plate} - {self.gear_position}"
