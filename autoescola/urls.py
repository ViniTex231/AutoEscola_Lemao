from django.contrib import admin
from django.urls import path, include
from App_Lemao.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include('App_Lemao.urls'))
]

admin.site.site_header = 'Auto Escola do Lemão'
admin.site.site_title = 'Auto Escola do Lemão'
admin.site.index_title = 'Sistema de Escalas'