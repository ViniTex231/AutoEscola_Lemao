from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Carros, Driver

# Create your views here.
def abre_index(request):
    return render(request, 'index.html')

def cad_carros(request):
    return render(request, 'carros.html')

def cad_drivers(request):
    return render(request, 'alunos.html')

def salvar_driver_novo(request):
    if (request.method == 'POST'):
        nome = request.POST.get('nomeDriver')
        data = request.POST.get('anoDriver')
        cnh = request.POST.get('cnhDriver')
        grava_driver = Driver(
            nome = nome,
            data = data,
            cnh = cnh,
        )
        grava_driver.save()
        messages.info(request, 'Motorista ' + nome + ' cadastrado com sucesso!')
        return render(request, 'alunos.html')
    
def salvar_carro_novo(request):
    if (request.method == 'POST'):
        nome = request.POST.get('nomeCarro')
        placa = request.POST.get('placaCarro')
        ano = request.POST.get('anoCarro')
        cor = request.POST.get('corCarro')
        dono = request.POST.get('donoCarro')
        grava_carro = Carros(
            nome = nome,
            placa = placa,
            ano = ano,
            cor = cor,
            dono = dono,
        )
        grava_carro.save()
        messages.info(request, 'Veículo ' + nome + ' cadastrado com sucesso!')
        return render(request, 'carros.html')