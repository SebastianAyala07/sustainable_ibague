from django.forms import ModelForm
from django.forms import TextInput, EmailInput, DateInput, FileInput, NumberInput
from django.utils.translation import gettext_lazy as _

from .models import Student, Driver


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = [
            'identification_card',
            'name',
            'surnames',
            'birth_date',
            'photo',
            'address',
            'phone',
            'email',
            'institution',
        ]
        labels = {
            'identification_card': _('Numero de documento'),
            'name': _('Nombres'),
            'surnames': _('Apellidos'),
            'birth_date': _('Fecha de cumpleaños'),
            'photo': _('Foto'),
            'address': _('Dirección'),
            'phone': _('Telefono'),
            'email': _('Correo electronico'),
            'institution': _('Institución'),
        }
        widgets = {
            'identification_card': NumberInput(attrs={'class': 'form-control no-background'}),
            'name': TextInput(attrs={'class': 'form-control no-background'}),
            'surnames': TextInput(attrs={'class': 'form-control no-background'}),
            'birth_date': DateInput(attrs={'class': 'form-control no-background', 'type':'date'}),
            'photo': FileInput(attrs={'class': 'form-control no-background'}),
            'address': TextInput(attrs={'class': 'form-control no-background'}),
            'phone': TextInput(attrs={'class': 'form-control no-background'}),
            'email': EmailInput(attrs={'class': 'form-control no-background'}),
            'institution': TextInput(attrs={'class': 'form-control no-background'}),
        }


class DriverForm(ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'
        labels = {
            'identification_card': _('Numero de documento'),
            'name': _('Nombres'),
            'surnames': _('Apellidos'),
            'birth_date': _('Fecha de cumpleaños'),
            'photo': _('Foto'),
            'address': _('Dirección'),
            'phone': _('Telefono'),
            'email': _('Correo electronico'),
            'type_of_license': _('Tipo de licencia'),
            'license_issue_date': _('Fecha expedicion licencia')
        }
        widgets = {
            'identification_card': NumberInput(attrs={'class': 'form-control no-background'}),
            'name': TextInput(attrs={'class': 'form-control no-background'}),
            'surnames': TextInput(attrs={'class': 'form-control no-background'}),
            'birth_date': DateInput(attrs={'class': 'form-control no-background', 'type':'date'}),
            'photo': FileInput(attrs={'class': 'form-control no-background'}),
            'address': TextInput(attrs={'class': 'form-control no-background'}),
            'phone': TextInput(attrs={'class': 'form-control no-background'}),
            'email': EmailInput(attrs={'class': 'form-control no-background'}),
            'type_of_license': TextInput(attrs={'class': 'form-control no-background', 'placeholder': 'Ex: A1 o A2'}),
            'license_issue_date': DateInput(attrs={'class': 'form-control no-background', 'type':'date'})
        }
