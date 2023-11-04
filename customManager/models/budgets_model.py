from django.db import models
from customManager.models.base_model import Base
from security.models import CustomUser

class Budget(Base):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='budgets')
    name = models.CharField('Nome', max_length=255)
    description = models.TextField('Descrição')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[('PENDING', 'Pendente'), ('ACCEPTED', 'Aceito'), ('DECLINED', 'Recusado')])

    class Meta:
        verbose_name = 'Orçamento'
        verbose_name_plural = 'Orçamento'
        indexes = [
                models.Index(fields=['status']),
            ]
    def __str__(self):
        return f'{self.name}'