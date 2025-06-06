from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'TipoMonitoramentoTipo'

router = routers.DefaultRouter()
router.register('', views.TipoMonitoramentoTipoViewSet, basename='TipoMonitoramentoTipo')

urlpatterns = [
    path('', include(router.urls) )
]
