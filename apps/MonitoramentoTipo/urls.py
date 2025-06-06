from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'MonitoramentoTipo'

router = routers.DefaultRouter()
router.register('', views.MonitoramentoTipoViewSet, basename='MonitoramentoTipo')

urlpatterns = [
    path('', include(router.urls) )
]
