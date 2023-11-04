from django.db import models
from telemetry.models.base_model import Base
from customManager.models.vehicle_model import Vehicle


class ElectricalSystemData(Base):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='electrical_system_data_related')
    battery_voltage = models.FloatField('Voltagem da Bateria')
    battery_current = models.FloatField('Corrente da Bateria')
    battery_charge = models.FloatField('Carga da Bateria')
    battery_state_of_charge = models.FloatField('Estado de Carga da Bateria')

    class Meta:
        verbose_name = "Dado do Sistema Elétrico"
        verbose_name_plural = "Dados do Sistema Elétrico"
        ordering = ['-deleted_at', '-updated_at', 'vehicle']
        indexes = [
            models.Index(fields=['battery_voltage']),
        ]

    def __str__(self):
        return f"{self.vehicle.plate} - {self.battery_voltage}V"
