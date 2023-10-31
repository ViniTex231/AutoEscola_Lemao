from django.shortcuts import render
from django.contrib import messages
from .models import Car, Driver, Service, Role, Employee, Schedule
from django.views.generic import ListView, TemplateView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ScheduleForm, DriverFilterForm, CarFilterForm


# Create your views here.

"""
class IndexView(TemplateView):
    template_name = 'login.html'

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        return context

class CarrosView(TemplateView):
    template_name = 'carros.html'

class DriversView(TemplateView):
    template_name = 'drivers.html'

#Create
class CreateCarroView(CreateView):
    model = Carros
    template_name = 'cad_carros.html'
    fields = ['nome', 'placa', 'ano', 'cor', 'dono']
    success_url = reverse_lazy('carros')

class CreateDriverView(CreateView):
    model = Driver
    template_name = 'cad_alunos.html'
    fields = ['nome', 'data', 'cnh']
    success_url = reverse_lazy('drivers')
#

#Read
class IndexCarroView(ListView):
    model = Carros
    template_name = 'cons_carros.html'
    context_object_name = 'carros'

    def get(self, request, *args, **kwargs):
        form = CarroFilterForm(request.GET)
        carros = self.get_queryset(form)
        return render(request, self.template_name, {'form': form, 'carros': carros})

    def post(self, request, *args, **kwargs):
        form = CarroFilterForm(request.POST)
        carros = self.get_queryset(form)
        return render(request, self.template_name, {'form': form, 'carros': carros})

    def get_queryset(self, form=None):
        queryset = Carros.objects.all()

        if form and form.is_valid():
            nome = form.cleaned_data.get('nome')
            placa = form.cleaned_data.get('placa')
            dono = form.cleaned_data.get('dono')

            if nome:
                queryset = queryset.filter(nome__icontains=nome)

            elif placa:
                queryset = queryset.filter(placa__icontains=placa)

            elif dono:
                queryset = queryset.filter(dono__icontains=dono)

        return queryset

class IndexDriverView(ListView):
    model = Driver
    template_name = 'cons_drivers.html'
    context_object_name = 'drivers'

    def get(self, request, *args, **kwargs):
        form = DriverFilterForm(request.GET)
        drivers = self.get_queryset(form)
        return render(request, self.template_name, {'form': form, 'drivers': drivers})

    def post(self, request, *args, **kwargs):
        form = DriverFilterForm(request.POST)
        drivers = self.get_queryset(form)
        return render(request, self.template_name, {'form': form, 'drivers': drivers})

    def get_queryset(self, form=None):
        queryset = Driver.objects.all()

        if form and form.is_valid():
            nome = form.cleaned_data.get('nome')
            cnh = form.cleaned_data.get('cnh')

            if nome:
                queryset = queryset.filter(nome__icontains=nome)

            if cnh:
                queryset = queryset.filter(cnh__icontains=cnh)

        return queryset
#

#Update
class UpdateCarroView(UpdateView):
    model = Carros
    template_name = 'cad_carros.html'
    fields = ['nome', 'placa', 'ano', 'cor', 'dono']
    success_url = reverse_lazy('carros')

class UpdateDriverView(UpdateView):
    model = Driver
    template_name = 'cad_alunos.html'
    fields = ['nome', 'data', 'cnh']
    success_url = reverse_lazy('drivers')
#

#Delete
class DeleteCarroView(DeleteView):
    model = Carros
    template_name = 'carro_del.html'
    success_url = reverse_lazy('carros')

class DeleteDriverView(DeleteView):
    model = Driver
    template_name = 'driver_del.html'
    success_url = reverse_lazy('drivers')
#

class AgendaView(TemplateView):
    template_name = "agenda.html"

class AgendaConsView(TemplateView):
    template_name = "cons_agenda.html"

    def get_context_data(self, **kwargs):
        context = super(AgendaConsView, self).get_context_data(**kwargs)
        context['agendas'] = Agenda.objects.all()
        return context
    
class AgendaDeleteView(DeleteView):
    model = Agenda
    success_url = reverse_lazy("agenda")
    template_name = "cons_agenda.html"

class AgendaFormView(FormView):
    template_name = "cad_agenda.html"
    form_class = AgendaForm
    success_url = reverse_lazy("cons_agenda")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.save()
        messages.success(self.request, 'Salvo com sucesso')
        return super().form_valid(form)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro')
        return super().form_invalid(form)
"""

#API V1