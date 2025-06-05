from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'EquipamentoItem'

router = routers.DefaultRouter()
router.register('', views.EquipamentoItemViewSet, basename='EquipamentoItem')

urlpatterns = [
    path('', include(router.urls) )
]
