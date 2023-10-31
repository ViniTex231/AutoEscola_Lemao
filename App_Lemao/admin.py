from django.contrib import admin
from .models import Service, Employee, Role, Schedule

# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('motorista', 'data', 'carro', 'dia', 'ativo', 'modificado')
