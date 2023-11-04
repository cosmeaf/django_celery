from django.db import models
from customManager.models.base_model import Base
from security.models import CustomUser


class ServiceHistory(Base):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='service_histories')
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descrição')
    date = models.DateField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Histório de Serviço"
        verbose_name_plural = "Histório de Serviços"
        ordering = ['-deleted_at', '-updated_at']
        indexes = [
                models.Index(fields=['name']),
            ]
    def __str__(self):
        return self.name