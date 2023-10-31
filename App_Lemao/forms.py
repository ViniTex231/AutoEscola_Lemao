from django import forms
from django.forms.widgets import DateInput
from .models import Schedule

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['motorista', 'data', 'carro', 'dia']
        widgets = {
            'data': DateInput(attrs={'type': 'date'})
        }

class DriverFilterForm(forms.Form):
    nome = forms.CharField(max_length=100, required=False)
    cnh = forms.CharField(max_length=20, required=False)

class CarFilterForm(forms.Form):
    nome = forms.CharField(max_length=50)
    placa = forms.CharField(max_length=8)
    dono = forms.CharField(max_length=20)
    