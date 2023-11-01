from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register('motoristas', DriverViewSet, basename='drivers')
router.register('carros', CarViewSet, basename='cars')
router.register('agendas', ScheduleViewSet, basename='schedules')
router.register('servicos', ServiceViewSet, basename='services')


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('home/', HomeView.as_view(), name='home'),
    path('carros/', CarrosView.as_view(), name='carros'),
    path('drivers/', DriversView.as_view(), name='drivers'),  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)