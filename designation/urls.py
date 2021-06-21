from django.urls import path, include

from rest_framework import routers
from rest_framework.routers import DefaultRouter

from . import views

routers = DefaultRouter()
routers.register(r'designation', views.DesignationViewsets,
                 basename='designation')
routers.register(r'department', views.DepartmentViewsets, basename='department')


urlpatterns = [
    path('', include(routers.urls)),
]
