from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'ClassEquipament'

router = routers.DefaultRouter()
router.register('', views.ClassEquipamentViewSet, basename='ClassEquipament')

urlpatterns = [
    path('', include(router.urls) )
]
