# customManager/views/address_view.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from dashboard.forms.address_form import AddressForm
from customManager.models.address_model import Address
import logging

logger = logging.getLogger(__name__)

@login_required
@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def list_addresses(request):
    if request.user.is_superuser:
        addresses = Address.objects.all()
    else:
        addresses = Address.objects.filter(user=request.user)
    return render(request, 'list_addresses.html', {'addresses': addresses})



@login_required
def add_address(request):
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addresses')
    else:
        form = AddressForm()
    return render(request, 'add_address.html', {'form': form})


@login_required
@user_passes_test(lambda u: u.is_superuser or u.addresses.filter(id=address_id).exists())
def edit_address(request, address_id):
    address = get_object_or_404(Address, id=address_id)
    if request.method == "POST":
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect('addresses')
    else:
        form = AddressForm(instance=address)
    return render(request, 'edit_address.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser or u.addresses.filter(id=address_id).exists())
def delete_address(request, address_id):
    address = get_object_or_404(Address, id=address_id)
    address.delete()
    return redirect('addresses')
