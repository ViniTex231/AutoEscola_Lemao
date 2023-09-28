from django import forms
from django.forms.widgets import DateInput
from .models import Agenda

class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ['motorista', 'data', 'carro']
        widgets = {
            'data': DateInput(attrs={'type': 'date'})
        }

class DriverFilterForm(forms.Form):
    nome = forms.CharField(max_length=100, required=False)
    cnh = forms.CharField(max_length=20, required=False)

class CarroFilterForm(forms.Form):
    nome = forms.CharField(max_length=50)
    placa = forms.CharField(max_length=8)
    dono = forms.CharField(max_length=20)
    