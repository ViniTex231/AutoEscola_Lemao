from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.abre_index, name='abre_index'),
    path('cad_carros', views.cad_carros, name='cad_carros'),
    path('cad_drivers', views.cad_drivers, name='cad_drivers'),
    path('salvar_driver_novo', views.salvar_driver_novo, name='salvar_driver_novo'),
    path('salvar_carro_novo', views.salvar_carro_novo, name='salvar_carro_novo')

]
