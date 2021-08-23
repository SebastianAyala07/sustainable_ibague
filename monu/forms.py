from django.forms.fields import ChoiceField
from persons.models import Driver, Student
from django.forms import ModelForm
from django.forms import TextInput, EmailInput, DateInput, FileInput, NumberInput, CheckboxInput
from django.forms.models import ModelChoiceField, ModelMultipleChoiceField
from django.forms.widgets import CheckboxSelectMultiple, TimeInput
from django.utils.translation import gettext_lazy as _

from .models import Vehicle, Service


class VehicleForm(ModelForm):
    driver = ModelChoiceField(queryset=Driver.objects.all())


    class Meta:
        model = Vehicle
        fields = '__all__'
        labels = {
            'license_plate': _('Placa'),
            'model': _('Modelo'),
            'brand': _('Marca'),
            'type_vehicle': _('Tipo de Vehiculo'),
            'photo': _('Foto'),
            'maximum_passengers': _('N° Maximo Pasajeros'),
            'fuel_type': _('Tipo de Combustible'),
            'available': _('Disponible'),
        }
        widgets = {
            'license_plate': TextInput(attrs={'class': 'form-control no-background'}),
            'model': NumberInput(attrs={'class': 'form-control no-background'}),
            'brand': TextInput(attrs={'class': 'form-control no-background'}),
            'type_vehicle': TextInput(attrs={'class': 'form-control no-background'}),
            'photo': FileInput(attrs={'class': 'form-control no-background'}),
            'maximum_passengers': NumberInput(attrs={'class': 'form-control no-background'}),
            'fuel_type': TextInput(attrs={'class': 'form-control no-background'}),
            'available': CheckboxInput(attrs={'class': 'form-control no-background'})
        }


class CustomMMCF(ModelMultipleChoiceField):
    def label_from_instance(self, member):
        return "%s" % member.name


class ServiceForm(ModelForm):

    vehicle_id = ModelChoiceField(queryset=Vehicle.objects.all())

    class Meta:
        model = Service
        fields = '__all__'
        labels = {
            'vehicle_id': _('Vehiculo'),
            'students_id': _('Estudiantes'),
            'date': _('Fecha'),
            'time': _('Hora'),
            'address': _('Dirección')
        }
        widgets = {
            'date': DateInput(attrs={'class': 'form-control no-background', 'type':'date'}),
            'time': TimeInput(attrs={'class': 'form-control no-background', 'type': 'time'}),
            'address': TextInput(attrs={'class': 'form-control no-background'})
        }

    students_id = CustomMMCF(
        queryset=Student.objects.all(),
        widget=CheckboxSelectMultiple
    )
