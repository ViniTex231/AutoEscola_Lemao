from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.abre_index, name='abre_index'),
    path('carros/', views.carros, name='carros'),
    path('drivers/', views.drivers, name='drivers'),
    path('cad_carros/', views.cad_carros, name='cad_carros'),
    path('cad_drivers/', views.cad_drivers, name='cad_drivers'),
    path('salvar_driver_novo/', views.salvar_driver_novo, name='salvar_driver_novo'),
    path('salvar_carro_novo/', views.salvar_carro_novo, name='salvar_carro_novo'),
    path('cons_carros/', views.cons_carros, name='cons_carros'),
    path('cons_drivers/', views.cons_drivers, name='cons_drivers'),
    path('edit_carros/<int:pk>/', views.edit_carros, name='edit_carros'),
    path('salvar_carro_editado/', views.salvar_carro_editado, name='salvar_carro_editado'),
    path('delete_carro/<int:id>', views.delete_carro, name='delete_carro'),
    path('delete_driver/<int:id>', views.delete_driver, name='delete_driver'),
    
]
