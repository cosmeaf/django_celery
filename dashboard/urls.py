from django.urls import path, include, re_path
from dashboard.views.vehicle_view import list_vehicles, add_vehicle, edit_vehicle, delete_vehicle
from dashboard.views.dashboard_view import DashboardView
from dashboard.views.addresses_view import list_addresses, add_address, edit_address, delete_address
from dashboard.views.custom_users_view import user_list, user_create, user_edit, user_delete, user_detail

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name="dashboard"),
    # Customers Views Data
    path('dashboard/users/', user_list, name="users"),
    path('dashboard/users/create/', user_create, name='user_create'),
    path('dashboard/users/users/<uuid:user_id>/', user_detail, name='user_detail'),
    path('dashboard/users/edit/<uuid:user_id>/', user_edit, name='user_edit'),
    path('dashboard/users/delete/<uuid:user_id>/', user_delete, name='user_delete'),
    # Address Views Data
    path('dashboard/addresses/', list_addresses, name="addresses"),
    path('dashboard/addresses/create/', add_address, name="add_address"),
    path('dashboard/addresses/edit/<uuid:address_id>', edit_address, name="edit_address"),
    path('dashboard/addresses/delete/<uuid:address_id>', delete_address, name="delete_address"),
    # Vehicles Views Data
    path('dashboard/vehicles/', list_vehicles, name='vehicles'),
    path('dashboard/vehicles/create/', add_vehicle, name='add_vehicle'),
    path('dashboard/vehicles/edit/<uuid:vehicle_id>/', edit_vehicle, name='edit_vehicle'),
    path('dashboard/vehicles/delete/<uuid:vehicle_id>/', delete_vehicle, name='delete_vehicle'),
]

