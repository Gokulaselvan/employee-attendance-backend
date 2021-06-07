from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import registration_view, ChangePasswordView, UserViewset

router = DefaultRouter()
router.register(r'users', UserViewset)
# router.register(r'users/change-password/<int:pk>/',)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', registration_view, name="register"),
    path('login/', obtain_auth_token, name="login"),
    path('change-password/<int:pk>/', ChangePasswordView.as_view(), name="change-password")
]