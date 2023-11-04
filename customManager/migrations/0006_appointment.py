# Generated by Django 4.2.6 on 2023-11-03 21:35

import customManager.models.appointment_model
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employeeInfo', '0001_initial'),
        ('customManager', '0005_testimonial_deleted_at_testimonial_updated_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Exclusão')),
                ('hour', models.CharField(help_text='Formato: 00:00', max_length=5, verbose_name='Hora do Serviço')),
                ('day', models.DateField(help_text='Formato: YYYY-MM-DD', verbose_name='Data do Serviço')),
                ('protocol', models.CharField(default=customManager.models.appointment_model.generate_protocol, max_length=22, unique=True, verbose_name='Protocolo')),
                ('cancellation_reason', models.TextField(blank=True, null=True, verbose_name='Justificativa para o cancelamento')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Appointment', related_query_name='schedule', to='customManager.address', verbose_name='Endereço')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employeeInfo.employeeinfo', verbose_name='Mecânico')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Appointment', related_query_name='schedule', to='customManager.services', verbose_name='Serviço')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Appointment', related_query_name='schedule', to='customManager.vehicle', verbose_name='Veículo')),
            ],
            options={
                'verbose_name': 'Agendamento',
                'verbose_name_plural': 'Agendamentos',
            },
        ),
    ]