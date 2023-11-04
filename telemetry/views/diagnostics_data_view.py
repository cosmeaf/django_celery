# views.py

from rest_framework import viewsets, permissions
from security.models import CustomUser
from telemetry.models.diagnostics_data_model import DiagnosticsData
from telemetry.serializers.diagnostics_data_serializer import DiagnosticsDataSerializer, DiagnosticsDataDetailSerializer

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.user == request.user

class DiagnosticsDataModelViewSet(viewsets.ModelViewSet):
    serializer_class = DiagnosticsDataSerializer
    queryset = DiagnosticsData.objects.all()

    def get_queryset(self):
        if self.request.user.is_staff:
            return self.queryset.all()
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        if self.request.user.is_staff and 'user' in serializer.validated_data:
            user_email = serializer.validated_data['user'].email
            user = CustomUser.objects.get(email=user_email)
            serializer.save(user=user)
        else:
            serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAuthenticated, IsOwner]

        return [permission() for permission in permission_classes]
