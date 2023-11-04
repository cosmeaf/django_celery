from rest_framework import serializers
from telemetry.models.brake_data_model import BrakeData
from customManager.models.vehicle_model import Vehicle

class BrakeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrakeData
        fields = (
            'id', 'vehicle', 'brake_temperature', 'brake_pad_wear', 'brake_disc_wear', 'brake_fluid_pressure'
        )
        read_only_fields = ('id',)

    def validate(self, data):
        user = self.context['request'].user
        if not Vehicle.objects.filter(user=user).exists():
            raise serializers.ValidationError("Usuário não possui veículo cadastrado. Cadastre um veículo antes de adicionar dados de freio.")
        return data


class BrakeDataDetailSerializer(BrakeDataSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = BrakeData
        fields = (
            'id', 'user', 'vehicle', 'brake_temperature', 'brake_pad_wear', 'brake_disc_wear', 'brake_fluid_pressure'
        )
        read_only_fields = ('id', 'user', 'vehicle')
