from rest_framework import serializers

from .models import UserProfile
from user.serializers import UserSerializer


class UserProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'
        depth = 2
