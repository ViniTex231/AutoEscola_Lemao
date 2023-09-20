from django.contrib import admin
from .models import Servico, Funcionario, Cargo, Agenda

# Register your models here.
@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')

@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ('motorista', 'data', 'carro', 'ativo', 'modificado')
