from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'Equipamento'

router = routers.DefaultRouter()
router.register('', views.ProductViewSet, basename='Equipamento')

urlpatterns = [
    path('', include(router.urls) )
]
