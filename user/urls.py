from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import registration_view, logout_view, ChangePasswordView, UserViewset

router = DefaultRouter()
router.register(r'users', UserViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', registration_view, name="register"),
    path('login/', obtain_auth_token, name="login"),
    path('logout/', logout_view, name="logout"),
    path('change-password/<int:pk>/',
         ChangePasswordView.as_view(), name="change-password")
]
