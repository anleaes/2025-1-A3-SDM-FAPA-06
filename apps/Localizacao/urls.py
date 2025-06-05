from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'Localizacao'

router = routers.DefaultRouter()
router.register('', views.LocalizacaoViewSet, basename='localizacao')

urlpatterns = [
    path('', include(router.urls) )
]
