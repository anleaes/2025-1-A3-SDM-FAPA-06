from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'ClasseEquipamento'

router = routers.DefaultRouter()
router.register('', views.ClasseEquipamentoViewSet, basename='ClasseEquipamento')

urlpatterns = [
    path('', include(router.urls) )
]
