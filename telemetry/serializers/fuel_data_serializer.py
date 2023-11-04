from rest_framework import serializers
from telemetry.models.fuel_data_model import FuelData
from customManager.models.vehicle_model import Vehicle

class FuelDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelData
        fields = (
            'id', 'vehicle', 'fuel_consumption', 'average_speed', 'fuel_efficiency', 'fuel_temperature', 'fuel_pressure'
        )
        read_only_fields = ('id',)

    def validate(self, data):
        user = self.context['request'].user
        if not Vehicle.objects.filter(user=user).exists():
            raise serializers.ValidationError("Usuário não possui veículo cadastrado. Cadastre um veículo antes de adicionar dados de combustível.")
        return data

class FuelDataDetailSerializer(FuelDataSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = FuelData
        fields = (
            'id', 'user', 'vehicle', 'fuel_consumption', 'average_speed', 'fuel_efficiency', 'fuel_temperature', 'fuel_pressure'
        )
        read_only_fields = ('id', 'user', 'vehicle')
