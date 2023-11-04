from django.db import models
from telemetry.models.base_model import Base
from customManager.models.vehicle_model import Vehicle


class DiagnosticsData(Base):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='diagnostics_data_related')
    code = models.CharField('Código', max_length=20)
    message = models.CharField('Mensagem', max_length=255)
    history = models.TextField('Histórico')

    class Meta:
        verbose_name = "Dado de Diagnóstico"
        verbose_name_plural = "Dados de Diagnóstico"
        ordering = ['-deleted_at', '-updated_at', 'vehicle', 'code']
        indexes = [
            models.Index(fields=['code']),
        ]

    def __str__(self):
        return f"{self.vehicle.plate} - {self.code}: {self.message[:20]}..."
