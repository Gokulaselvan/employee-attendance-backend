from django.urls import path, include

from rest_framework import routers
from rest_framework.routers import DefaultRouter

from . import views

routers = DefaultRouter()
routers.register(r'', views.ShiftViewset,
                 basename='shift')


urlpatterns = [
    path('', include(routers.urls)),
]