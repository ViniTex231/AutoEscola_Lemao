from django.urls import path, include
from . import views
from .views import IndexView, HomeView, CarrosView, DriversView, AgendaView, AgendaConsView, AgendaDeleteView, AgendaFormView, CreateCarroView, CreateDriverView, IndexCarroView, IndexDriverView, UpdateCarroView, UpdateDriverView, DeleteCarroView, DeleteDriverView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('home/', HomeView.as_view(), name='home'),
    path('carros/', CarrosView.as_view(), name='carros'),
    path('drivers/', DriversView.as_view(), name='drivers'),
    path('cad_carros/', CreateCarroView.as_view(), name='cad_carros'),
    path('cad_drivers/', CreateDriverView.as_view(), name='cad_drivers'),
    path('agenda/', AgendaView.as_view(), name='agenda'),
    path('cons_agenda/', AgendaConsView.as_view(), name='cons_agenda'),
    path('agenda/<int:pk>/delete/', AgendaDeleteView.as_view(), name="agenda_delete"),
    path('cad_agenda/', AgendaFormView.as_view(), name="cad_agenda"),
    path('cons_carros/', IndexCarroView.as_view(), name='cons_carros'),
    path('cons_drivers/', IndexDriverView.as_view(), name='cons_drivers'),
    path('<int:pk>/updatec/', UpdateCarroView.as_view(), name='upd_carro'),
    path('<int:pk>/updated/', UpdateDriverView.as_view(), name='upd_driver'),
    path('<int:pk>/deletec/', DeleteCarroView.as_view(), name='del_carro'),
    path('<int:pk>/deleted/', DeleteDriverView.as_view(), name='del_driver'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)