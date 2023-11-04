# dashboard/views/vehicle_view.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from dashboard.forms.vehicle_form import VehicleForm
from customManager.models.vehicle_model import Vehicle
import logging

logger = logging.getLogger(__name__)

@login_required
@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def list_vehicles(request):
    if request.user.is_superuser:
        vehicles = Vehicle.objects.all()
    else:
        vehicles = Vehicle.objects.filter(user=request.user)
    return render(request, 'list_vehicles.html', {'vehicles': vehicles})

@login_required
def add_vehicle(request):
    if request.method == "POST":
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicles')
    else:
        form = VehicleForm()
    return render(request, 'add_vehicle.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser or u.vehicles.filter(id=vehicle_id).exists())
def edit_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    if request.method == "POST":
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicles')
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'edit_vehicle.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser or u.vehicles.filter(id=vehicle_id).exists())
def delete_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    vehicle.delete()
    return redirect('vehicles')
