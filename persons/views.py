from django.shortcuts import redirect, render

from .forms import DriverForm, StudentForm

def student_create_view(request):
    form = StudentForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        form = StudentForm()
        return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'product_create.html', context)

def driver_create_view(request):
    form = DriverForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        form = DriverForm()
        return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'driver_create.html', context)
