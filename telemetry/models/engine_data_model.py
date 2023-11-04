from django.db import models
from telemetry.models.base_model import Base
from customManager.models.vehicle_model import Vehicle


class EngineData(Base):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='engine_data_related')
    temperature_engine_coolant = models.FloatField('Temperatura do Líquido de Arrefecimento')
    oil_pressure = models.FloatField('Pressão do Óleo')
    engine_oil_temperature = models.FloatField('Temperatura do Óleo do Motor')
    engine_speed = models.IntegerField('Rotação do Motor')
    engine_load = models.FloatField('Carga do Motor')
    throttle_position = models.FloatField('Posição do Acelerador')
    air_fuel_ratio = models.FloatField('Relação Ar-Combustível')
    intake_manifold_pressure = models.FloatField('Pressão no Coletor de Admissão')
    intake_air_temperature = models.FloatField('Temperatura do Ar de Admissão')
    fuel_pressure = models.FloatField('Pressão do Combustível')
    oxygen_sensor_voltage = models.FloatField('Tensão do Sensor de Oxigênio')
    crankshaft_position = models.FloatField('Posição do Virabrequim')
    camshaft_position = models.FloatField('Posição do Eixo de Comando')

    class Meta:
        verbose_name = 'Dados do Motor'
        verbose_name_plural = 'Dados dos Motores'

        indexes = [
            models.Index(fields=['temperature_engine_coolant']),
        ]
               
    def __str__(self):
        return self.vehicle.plate
