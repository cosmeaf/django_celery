from rest_framework import serializers
from telemetry.models.electrical_system_data_model import ElectricalSystemData
from customManager.models.vehicle_model import Vehicle

class ElectricalSystemDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectricalSystemData
        fields = (
            'id', 'vehicle', 'battery_voltage', 'battery_current', 'battery_charge', 'battery_state_of_charge'
        )
        read_only_fields = ('id',)

    def validate(self, data):
        user = self.context['request'].user
        if not Vehicle.objects.filter(user=user).exists():
            raise serializers.ValidationError("Usuário não possui veículo cadastrado. Cadastre um veículo antes de adicionar dados do sistema elétrico.")
        return data

class ElectricalSystemDataDetailSerializer(ElectricalSystemDataSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ElectricalSystemData
        fields = (
            'id', 'user', 'vehicle', 'battery_voltage', 'battery_current', 'battery_charge', 'battery_state_of_charge'
        )
        read_only_fields = ('id', 'user', 'vehicle')
