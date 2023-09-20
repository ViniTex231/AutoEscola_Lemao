from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Carros, Driver, Servico, Funcionario
from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        return context

class CarrosView(TemplateView):
    template_name = 'carros.html'

class DriversView(TemplateView):
    template_name = 'drivers.html'

class CadCarrosView(TemplateView):
    template_name = 'cad_carros.html'

class CadDriversView(TemplateView):
    template_name = 'cad_alunos.html'

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
        return render(request, 'cad_alunos.html')
    
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
        return render(request, 'cad_carros.html')
    
def cons_carros(request):
    dado_pesquisa_nome = request.POST.get('nomeCarro')
    dado_pesquisa_placa = request.POST.get('placaCarro')
    dado_pesquisa_dono = request.POST.get('donoCarro')

    if dado_pesquisa_nome or dado_pesquisa_placa or dado_pesquisa_dono:
        page = request.GET.get('page')

        if page:
            dado_pesquisa = request.GET.get(dado_pesquisa)
            carros_lista = Carros.objects.filter(nome__icontains=dado_pesquisa_nome)
            paginas = Paginator(carros_lista, 10000)
            carros = paginas.get_page(page)

            return render(request, 'cons_carros.html', {'dados_carros' : carros, 'dado_pesquisa' : dado_pesquisa})
        
        if dado_pesquisa_nome != None and dado_pesquisa_nome != '':
            carros_lista = Carros.objects.filter(nome__icontains=dado_pesquisa_nome)
            paginas = Paginator(carros_lista, 10000)
            page = request.GET.get('page')
            carros = paginas.get_page(page)

            return render(request, 'cons_carros.html', {'dados_carros' : carros, 'dado_pesquisa' : dado_pesquisa_nome})
        
        elif dado_pesquisa_placa != None and dado_pesquisa_placa != '':
            carros = Carros.objects.filter(cnh__icontains=dado_pesquisa_placa)
            return render(request, 'cons_carros.html', {'dados_carros' : carros})
        
        elif dado_pesquisa_dono != None and dado_pesquisa_dono != '':
            carros = Carros.objects.filter(dono__icontains=dado_pesquisa_dono)
            return render(request, 'cons_carros.html', {'dados_carros' : carros})
        
        else:
            return render(request, 'cons_carros.html')
    else:
        carros = Carros.objects.all()
        return render(request, 'cons_carros.html', {'dados_carros' : carros})
    
def cons_drivers(request):
    dado_pesquisa_nome = request.POST.get('nomeDriver')
    dado_pesquisa_cnh = request.POST.get('cnhDriver')

    if dado_pesquisa_nome or dado_pesquisa_cnh:
        page = request.GET.get('page')

        if page:
            dado_pesquisa = request.GET.get(dado_pesquisa)
            drivers_lista = Driver.objects.filter(nome__icontains=dado_pesquisa_nome)
            paginas = Paginator(drivers_lista, 10000)
            drivers = paginas.get_page(page)

            return render(request, 'cons_drivers.html', {'dados_drivers' : drivers, 'dado_pesquisa' : dado_pesquisa})
        
        if dado_pesquisa_nome != None and dado_pesquisa_nome != '':
            drivers_lista = Driver.objects.filter(nome__icontains=dado_pesquisa_nome)
            paginas = Paginator(drivers_lista, 10000)
            page = request.GET.get('page')
            drivers = paginas.get_page(page)

            return render(request, 'cons_drivers.html', {'dados_drivers' : drivers, 'dado_pesquisa' : dado_pesquisa_nome})
        
        elif dado_pesquisa_cnh != None and dado_pesquisa_cnh != '':
            drivers = Driver.objects.filter(cnh__icontains=dado_pesquisa_cnh)
            return render(request, 'cons_drivers.html', {'dados_drivers' : drivers})
        
        else:
            return render(request, 'cons_drivers.html')
    else:
        drivers = Driver.objects.all()
        return render(request, 'cons_drivers.html', {'dados_drivers' : drivers})
    
def edit_carros(request, pk):
    dados_editar = get_object_or_404(Carros, id=pk)
    return render(request, 'edit_carros.html', {'dados_carros' : dados_editar})

def salvar_carro_editado(request):
    if request.method == 'POST':
        id_carro = request.POST.get('id_carro')
        nomeCarro = request.POST.get('nomeCarro')
        placaCarro = request.POST.get('placaCarro')
        corCarro = request.POST.get('corCarro')
        donoCarro = request.POST.get('donoCarro')

        carro_editado = Carros.objects.get(id=id_carro)

        carro_editado.nomeCarro = nomeCarro
        carro_editado.placaCarro = placaCarro
        carro_editado.corCarro = corCarro
        carro_editado.donoCarro = donoCarro

        carro_editado.save()

        messages.info(request, 'Carro ' + nomeCarro + ' editado com sucesso!')
        return render(request, 'cons_carros.html')

def delete_carro(request, id):
    carro_deletado = get_object_or_404(Carros, pk=id)
    nome = carro_deletado.nome
    carro_deletado.delete()

    messages.info(request, 'Carro ' + nome + ' deletado com sucesso!')
    return redirect('cons_carros')

def delete_driver(request, id):
    driver_deletado = get_object_or_404(Driver, pk=id)
    nome = driver_deletado.nome
    driver_deletado.delete()

    messages.info(request, 'Motorista ' + nome + ' deletado com sucesso!')
    return redirect('cons_drivers')
