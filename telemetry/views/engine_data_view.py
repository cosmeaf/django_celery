from rest_framework import viewsets, permissions
from security.models import CustomUser
from customManager.models.vehicle_model import Vehicle
from telemetry.models.engine_data_model import EngineData
from telemetry.serializers.engine_data_serializer import EngineDataSerializer, EngineDataDetailSerializer

# IsAuthenticated AllowAny
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.vehicle.user == request.user


class EngineDataModelViewSet(viewsets.ModelViewSet):
    serializer_class = EngineDataSerializer
    queryset = EngineData.objects.all()

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

    def get_serializer_class(self):
        if self.action in ['create', 'list']:
            return EngineDataSerializer
        return EngineDataDetailSerializer


