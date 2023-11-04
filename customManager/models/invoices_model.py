from django.db import models
from customManager.models.base_model import Base
from security.models import CustomUser


class Invoice(Base):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='invoices')
    invoice_number = models.CharField('Numero Pedido', max_length=50)
    total_amount = models.DecimalField('Total', max_digits=10, decimal_places=2)
    due_date = models.DateField('Data')
    status = models.CharField('Andamento', max_length=50, choices=[('PAID', 'Pago'), ('UNPAID', 'Não Pago'), ('OVERDUE', 'Vencido')])

    class Meta:
        verbose_name = 'Orçamento'
        verbose_name_plural = 'Orçamento'
        indexes = [
                models.Index(fields=['invoice_number']),
            ]
    def __str__(self):
        return f'{self.invoice_number}'