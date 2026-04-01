from django import forms
from .models import Paciente, Doctor, HoraMedica

WIDGET_ATTRS = {'class': 'form-control'}

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs=WIDGET_ATTRS),
            'apellido': forms.TextInput(attrs=WIDGET_ATTRS),
            'edad': forms.NumberInput(attrs=WIDGET_ATTRS),
            'fecha_nacimiento': forms.DateInput(attrs={**WIDGET_ATTRS, 'type': 'date'}),
        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs=WIDGET_ATTRS),
            'apellido': forms.TextInput(attrs=WIDGET_ATTRS),
            'edad': forms.NumberInput(attrs=WIDGET_ATTRS),
            'fecha_nacimiento': forms.DateInput(attrs={**WIDGET_ATTRS, 'type': 'date'}),
            'especialidad': forms.TextInput(attrs=WIDGET_ATTRS),
        }

class HoraMedicaForm(forms.ModelForm):
    class Meta:
        model = HoraMedica
        fields = '__all__'
        widgets = {
            'paciente': forms.Select(attrs=WIDGET_ATTRS),
            'doctor': forms.Select(attrs=WIDGET_ATTRS),
            'hora': forms.TimeInput(attrs={**WIDGET_ATTRS, 'type': 'time'}),
            'fecha': forms.DateInput(attrs={**WIDGET_ATTRS, 'type': 'date'}),
            'motivo': forms.Textarea(attrs={**WIDGET_ATTRS, 'rows': 3}),
        }