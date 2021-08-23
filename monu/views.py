from monu.forms import VehicleForm, ServiceForm
from django.shortcuts import redirect, render


def create_vehicle_view(request):
    form = VehicleForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        form = VehicleForm()
        return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'vehicle_create.html', context)

def create_service_view(request):
    form = ServiceForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        form = ServiceForm()
        return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'service_create.html', context)
