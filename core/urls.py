from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

# ROUTES Telemetry
from telemetry.views.engine_data_view import EngineDataModelViewSet
from telemetry.views.brake_data_view import BrakeDataModelViewSet
from telemetry.views.cooling_system_data_view import CoolingSystemDataModelViewSet
from telemetry.views.diagnostics_data_view import DiagnosticsDataModelViewSet
from telemetry.views.electrical_system_data_view import ElectricalSystemDataModelViewSet
from telemetry.views.fuel_data_view import FuelDataModelViewSet

# ROUTES Custom Manager
from customManager.views.address_view import AddressModelViewSet
from customManager.views.vehicle_view import VehicleModelViewSet
from customManager.views.user_view import CustomUserModelViewSet
from customManager.views.services_view import ServiceModelViewSet, HourServiceModelViewSet

# Default Route Django Rest Framework
router = DefaultRouter()
router.register(r'brake-data', BrakeDataModelViewSet, basename='brake_data')
router.register(r'cooling-system-data', CoolingSystemDataModelViewSet, basename='cooling_system_data')
router.register(r'diagnostics-data', DiagnosticsDataModelViewSet, basename='diagnostics_data')
router.register(r'electrical-system-data', ElectricalSystemDataModelViewSet, basename='electrical_system_data')
router.register(r'engine-data', EngineDataModelViewSet, basename='engine_data')
router.register(r'fuel-data', FuelDataModelViewSet, basename='fuel_data')

# Default Route Custom Manager
router.register(r'users', CustomUserModelViewSet, basename='users')
router.register(r'addresses', AddressModelViewSet, basename='addresses')
router.register(r'vehicles', VehicleModelViewSet, basename='vehicles')
router.register(r'service', ServiceModelViewSet, basename='service')
router.register(r'hourservice', HourServiceModelViewSet, basename='hourservice')


urlpatterns = [
    path('', include('web.urls')),
    path('', include('dashboard.urls')),
    path('admin/', admin.site.urls),
    # path('', include('admin_argon.urls')),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/', include((router.urls))),
    re_path(r'api/', include(router.urls)),
    path('api/', include('security.urls')),

]

# Site Custom
# admin.site.index_title = settings.INDEX_TITLE
# admin.site.site_header = settings.ADMIN_SITE_HEADER
# admin.site.site_title = settings.ADMIN_SITE_TITLE

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)