from rest_framework import serializers
from telemetry.models.cooling_system_data_model import CoolingSystemData
from customManager.models.vehicle_model import Vehicle
from security.models import CustomUser
from rest_framework.exceptions import ValidationError

class CoolingSystemDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoolingSystemData
        fields = (
            'id', 'vehicle', 'coolant_temperature', 'coolant_pressure', 'coolant_flow'
        )
        read_only_fields = ('id',)

    def validate(self, data):
        user = self.context['request'].user
        if not Vehicle.objects.filter(user=user).exists():
            raise serializers.ValidationError("Usuário não possui veículo cadastrado. Cadastre um veículo antes de adicionar dados do sistema de resfriamento.")
        return data


class CoolingSystemDataDetailSerializer(CoolingSystemDataSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CoolingSystemData
        fields = (
            'id', 'user', 'vehicle', 'coolant_temperature', 'coolant_pressure', 'coolant_flow'
        )
        read_only_fields = ('id', 'user', 'vehicle')
