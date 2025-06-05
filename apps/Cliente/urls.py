from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'Cliente'

router = routers.DefaultRouter()
router.register('', views.ClienteViewSet, basename='Cliente')

urlpatterns = [
    path('', include(router.urls) )
]
