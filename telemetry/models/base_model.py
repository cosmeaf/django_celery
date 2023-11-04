from django.db import models
import uuid

class Base(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField('Criação', auto_now_add=True)
    updated_at = models.DateTimeField('Atualização', auto_now=True)
    deleted_at = models.DateTimeField('Exclusão', null=True, blank=True, db_index=True)

    class Meta:
        abstract = True
        verbose_name = 'Base Model'
        verbose_name_plural = 'Bases Models'
    
    def delete(self, using=None, keep_parents=False):
        self.deleted_at = models.DateTimeField(auto_now=True)
        self.save()
