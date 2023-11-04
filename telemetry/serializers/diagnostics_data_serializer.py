from rest_framework import serializers
from telemetry.models.diagnostics_data_model import DiagnosticsData
from customManager.models.vehicle_model import Vehicle

class DiagnosticsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosticsData
        fields = (
            'id', 'vehicle', 'code', 'message', 'history'
        )
        read_only_fields = ('id',)

    def validate(self, data):
        user = self.context['request'].user
        if not Vehicle.objects.filter(user=user).exists():
            raise serializers.ValidationError("Usuário não possui veículo cadastrado. Cadastre um veículo antes de adicionar dados de diagnóstico.")
        return data

class DiagnosticsDataDetailSerializer(DiagnosticsDataSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = DiagnosticsData
        fields = (
            'id', 'user', 'vehicle', 'code', 'message', 'history'
        )
        read_only_fields = ('id', 'user', 'vehicle')
