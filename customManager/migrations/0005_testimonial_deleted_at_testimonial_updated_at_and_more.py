# Generated by Django 4.2.6 on 2023-11-02 09:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customManager', '0004_testimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Exclusão'),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Atualização'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
