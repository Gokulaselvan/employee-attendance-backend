from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


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
            employee_id = self.validated_data['employee_id']
        )

        password = self.validated_data['password']
        retype_password = self.validated_data['retype_password']

        if password != retype_password:

            raise serializers.ValidationError({'password': "Passwords must match."})
        
        user.set_password(password)
        user.save()
        return user
        

