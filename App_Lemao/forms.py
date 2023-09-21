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
