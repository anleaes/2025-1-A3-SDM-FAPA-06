from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'Monitoramento'

router = routers.DefaultRouter()
router.register('', views.MonitoramentoViewSet, basename='Monitoramento')

urlpatterns = [
    path('', include(router.urls) )
]