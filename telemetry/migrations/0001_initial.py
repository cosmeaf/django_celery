# Generated by Django 4.2.6 on 2023-10-27 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customManager', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EngineData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Exclusão')),
                ('temperature_engine_coolant', models.FloatField(verbose_name='Temperatura do Líquido de Arrefecimento')),
                ('oil_pressure', models.FloatField(verbose_name='Pressão do Óleo')),
                ('engine_oil_temperature', models.FloatField(verbose_name='Temperatura do Óleo do Motor')),
                ('engine_speed', models.IntegerField(verbose_name='Rotação do Motor')),
                ('engine_load', models.FloatField(verbose_name='Carga do Motor')),
                ('throttle_position', models.FloatField(verbose_name='Posição do Acelerador')),
                ('air_fuel_ratio', models.FloatField(verbose_name='Relação Ar-Combustível')),
                ('intake_manifold_pressure', models.FloatField(verbose_name='Pressão no Coletor de Admissão')),
                ('intake_air_temperature', models.FloatField(verbose_name='Temperatura do Ar de Admissão')),
                ('fuel_pressure', models.FloatField(verbose_name='Pressão do Combustível')),
                ('oxygen_sensor_voltage', models.FloatField(verbose_name='Tensão do Sensor de Oxigênio')),
                ('crankshaft_position', models.FloatField(verbose_name='Posição do Virabrequim')),
                ('camshaft_position', models.FloatField(verbose_name='Posição do Eixo de Comando')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='engine_data', to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='engine_data_related', to='customManager.vehicle')),
            ],
            options={
                'verbose_name': 'Dados do Motor',
                'verbose_name_plural': 'Dados dos Motores',
            },
        ),
        migrations.CreateModel(
            name='TransmissionData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Exclusão')),
                ('transmission_fluid_temperature', models.FloatField(verbose_name='Temperatura do Fluido da Transmissão')),
                ('transmission_fluid_pressure', models.FloatField(verbose_name='Pressão do Fluido da Transmissão')),
                ('transmission_speed', models.IntegerField(verbose_name='Velocidade da Transmissão')),
                ('gear_position', models.CharField(max_length=20, verbose_name='Posição da Engrenagem')),
                ('transmission_ratio', models.FloatField(verbose_name='Relação da Transmissão')),
                ('transmission_torque', models.FloatField(verbose_name='Torque da Transmissão')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transmission_data_related', to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transmission_data_related', to='customManager.vehicle')),
            ],
            options={
                'verbose_name': 'Dado de Transmissão',
                'verbose_name_plural': 'Dados de Transmissão',
                'ordering': ['-deleted_at', '-updated_at', 'vehicle'],
                'indexes': [models.Index(fields=['gear_position'], name='telemetry_t_gear_po_3a85c3_idx')],
                'unique_together': {('vehicle', 'gear_position')},
            },
        ),
        migrations.CreateModel(
            name='FuelData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Exclusão')),
                ('fuel_consumption', models.FloatField(verbose_name='Consumo de Combustível')),
                ('average_speed', models.FloatField(verbose_name='Velocidade Média')),
                ('fuel_efficiency', models.FloatField(verbose_name='Eficiência de Combustível')),
                ('fuel_temperature', models.FloatField(verbose_name='Temperatura do Combustível')),
                ('fuel_pressure', models.FloatField(verbose_name='Pressão do Combustível')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fuel_data_related', to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fuel_data_related', to='customManager.vehicle')),
            ],
            options={
                'verbose_name': 'Dado de Combustível',
                'verbose_name_plural': 'Dados de Combustível',
                'ordering': ['-deleted_at', '-updated_at', 'vehicle'],
                'indexes': [models.Index(fields=['fuel_consumption'], name='telemetry_f_fuel_co_f8e6f6_idx')],
            },
        ),
        migrations.CreateModel(
            name='ElectricalSystemData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Exclusão')),
                ('battery_voltage', models.FloatField(verbose_name='Voltagem da Bateria')),
                ('battery_current', models.FloatField(verbose_name='Corrente da Bateria')),
                ('battery_charge', models.FloatField(verbose_name='Carga da Bateria')),
                ('battery_state_of_charge', models.FloatField(verbose_name='Estado de Carga da Bateria')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='electrical_system_data_related', to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='electrical_system_data_related', to='customManager.vehicle')),
            ],
            options={
                'verbose_name': 'Dado do Sistema Elétrico',
                'verbose_name_plural': 'Dados do Sistema Elétrico',
                'ordering': ['-deleted_at', '-updated_at', 'vehicle'],
                'indexes': [models.Index(fields=['battery_voltage'], name='telemetry_e_battery_6a10fc_idx')],
            },
        ),
        migrations.CreateModel(
            name='DiagnosticsData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Exclusão')),
                ('code', models.CharField(max_length=20, verbose_name='Código')),
                ('message', models.CharField(max_length=255, verbose_name='Mensagem')),
                ('history', models.TextField(verbose_name='Histórico')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diagnostics_data_related', to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diagnostics_data_related', to='customManager.vehicle')),
            ],
            options={
                'verbose_name': 'Dado de Diagnóstico',
                'verbose_name_plural': 'Dados de Diagnóstico',
                'ordering': ['-deleted_at', '-updated_at', 'vehicle', 'code'],
                'indexes': [models.Index(fields=['code'], name='telemetry_d_code_f73adb_idx')],
            },
        ),
        migrations.CreateModel(
            name='CoolingSystemData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Exclusão')),
                ('coolant_temperature', models.FloatField(verbose_name='Temperatura do Refrigerante')),
                ('coolant_pressure', models.FloatField(verbose_name='Pressão do Refrigerante')),
                ('coolant_flow', models.FloatField(verbose_name='Fluxo do Refrigerante')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cooling_system_data_related', to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cooling_system_data_related', to='customManager.vehicle')),
            ],
            options={
                'verbose_name': 'Dado do Sistema de Resfriamento',
                'verbose_name_plural': 'Dados do Sistema de Resfriamento',
                'ordering': ['-deleted_at', '-updated_at', 'vehicle'],
                'indexes': [models.Index(fields=['coolant_temperature'], name='telemetry_c_coolant_71563c_idx')],
            },
        ),
        migrations.CreateModel(
            name='BrakeData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Exclusão')),
                ('brake_temperature', models.FloatField(verbose_name='Temperatura do Freio')),
                ('brake_pad_wear', models.FloatField(verbose_name='Desgaste da Pastilha de Freio')),
                ('brake_disc_wear', models.FloatField(verbose_name='Desgaste do Disco de Freio')),
                ('brake_fluid_pressure', models.FloatField(verbose_name='Pressão do Fluido de Freio')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brake_data_related', to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brake_data_related', to='customManager.vehicle')),
            ],
            options={
                'verbose_name': 'Dado de Freio',
                'verbose_name_plural': 'Dados de Freio',
                'ordering': ['-deleted_at', '-updated_at', 'vehicle'],
                'indexes': [models.Index(fields=['brake_temperature'], name='telemetry_b_brake_t_a7990c_idx')],
            },
        ),
    ]