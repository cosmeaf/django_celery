from django.shortcuts import render, redirect, get_object_or_404
from security.models import CustomUser
from dashboard.forms.custom_user_form import CustomUserForm, AddressFormSet, VehicleFormSet, AppointmentFormSet
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
import logging

logger = logging.getLogger(__name__)

@login_required(login_url="/login/")
def user_list(request):
    if request.user.is_superuser:
        users = CustomUser.objects.all()
        superusers = users.filter(is_superuser=True)
        regular_users = users.filter(is_superuser=False)
    else:
        superusers = CustomUser.objects.none() 
        regular_users = CustomUser.objects.filter(id=request.user.id)

    return render(request, 'list_users.html', {
        'superusers': superusers,
        'regular_users': regular_users
    })


@login_required(login_url="/login/")
def user_detail(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    
    if request.user.is_superuser or request.user.id == user_id:
        if request.method == 'POST':
            form = CustomUserForm(request.POST, request.FILES, instance=user, context={'request': request})
            address_formset = AddressFormSet(request.POST, instance=user)
            vehicle_formset = VehicleFormSet(request.POST, instance=user)
            appointment_formset = AppointmentFormSet(request.POST, instance=user)

            if form.is_valid() and address_formset.is_valid() and vehicle_formset.is_valid() and appointment_formset.is_valid():
                form.save()
                address_formset.save()
                vehicle_formset.save()
                appointment_formset.save()
                messages.success(request, "Perfil atualizado com sucesso.")
                return redirect('user_detail', user_id=user_id)
            else:
                messages.error(request, "Foram encontrados erros no formulário.")
        else:
            form = CustomUserForm(instance=user)
            address_formset = AddressFormSet(instance=user)
            vehicle_formset = VehicleFormSet(instance=user)
            appointment_formset = AppointmentFormSet(instance=user)
        
        context = {
            'form': form,
            'address_formset': address_formset,
            'vehicle_formset': vehicle_formset,
            'appointment_formset': appointment_formset,
            'user': user
        }
        return render(request, 'user_detail.html', context)
    else:
        messages.error(request, "Você não tem permissão para ver esses detalhes.")
        return redirect('users')


@login_required(login_url="/login/")
@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES, request=request)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário criado com sucesso!')
            return redirect('users')
    else:
        form = CustomUserForm()
    return render(request, 'user_form.html', {'form': form})


@login_required(login_url="/login/")
@user_passes_test(lambda u: u.is_superuser)
def user_edit(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES, request=request)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário atualizado com sucesso!')
            return redirect('users')
    else:
        form = CustomUserForm(instance=user)
    return render(request, 'user_form.html', {'form': form})

@login_required(login_url="/login/")
@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Usuário excluído com sucesso!')
        return redirect('users')
    return render(request, 'user_confirm_delete.html', {'user': user})
