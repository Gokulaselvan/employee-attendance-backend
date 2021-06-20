from django.shortcuts import render
from django.contrib.auth import get_user_model


from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import status

from .serializers import ChangePasswordSerializer, RegisterSerializer, UserSerializer

User = get_user_model()


@api_view(["POST"])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)

        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "successfully registered a new user"
            data['email'] = user.email
            data['username'] = user.username
            data['employee_id'] = user.employee_id

            return Response(data, status=status.HTTP_201_CREATED)

        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def logout_view(request):

    request.user.auth_token.delete()
    return Response(data={"success": "Successfully Logged out"}, status=status.HTTP_204_NO_CONTENT)


class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class UserViewset(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ]
