from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from security.models import CustomUser
from customManager.models.vehicle_model import Vehicle
from telemetry.models.engine_data_model import EngineData

class EngineDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngineData
        fields = (
            'id', 'vehicle', 'temperature_engine_coolant', 'oil_pressure', 'engine_oil_temperature', 
            'engine_speed', 'engine_load', 'throttle_position', 'air_fuel_ratio', 'intake_manifold_pressure', 
            'intake_air_temperature', 'fuel_pressure', 'oxygen_sensor_voltage', 'crankshaft_position', 
            'camshaft_position'
        )
        read_only_fields = ('id',)

    def validate(self, data):
        user = self.context['request'].user
        if not Vehicle.objects.filter(user=user).exists():
            raise serializers.ValidationError("Usuário não possui veículo cadastrado. Cadastre um veículo antes de adicionar dados do motor.")
        return data


class EngineDataDetailSerializer(EngineDataSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = EngineData
        fields = (
            'id', 'user', 'vehicle', 'temperature_engine_coolant', 'oil_pressure', 'engine_oil_temperature', 
            'engine_speed', 'engine_load', 'throttle_position', 'air_fuel_ratio', 'intake_manifold_pressure', 
            'intake_air_temperature', 'fuel_pressure', 'oxygen_sensor_voltage', 'crankshaft_position', 
            'camshaft_position'
        )
        read_only_fields = ('id', 'user', 'vehicle')