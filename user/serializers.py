from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['password', 'groups', 'user_permissions']

class RegisterSerializer(serializers.ModelSerializer):

    retype_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'employee_id',
                  'password', 'retype_password', ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            employee_id=self.validated_data['employee_id']
        )

        password = self.validated_data['password']
        retype_password = self.validated_data['retype_password']

        if password != retype_password:

            raise serializers.ValidationError(
                {'password': "Passwords must match."})

        user.set_password(password)
        user.save()
        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    retype_password = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("old_password", "password", "retype_password")
        extra_kwargs = {
            'password': {'write_only': True},
            'retype_password': {'write_only': True},
            'old_password': {'write_only': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['retype_password']:
            raise serializers.ValidationError(
                {"password": "Passwords fields didn't match"})

        return super().validate(attrs)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                {"old_password": "Old password is not correct"})

        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])

        instance.save()

        return instance
