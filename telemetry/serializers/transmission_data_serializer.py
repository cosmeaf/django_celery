from rest_framework import serializers
from telemetry.models.transmission_data_model import TransmissionData

class TransmissionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransmissionData
        fields = '__all__'