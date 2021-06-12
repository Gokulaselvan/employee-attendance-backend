from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserProfile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Need to change it as foreign key field
    designation = models.CharField(max_length=50)

    # Need to change it as foreign key field
    department = models.CharField(max_length=50)
    # Need to add Profile picture field

    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    joining_date = models.DateField(auto_now=False, auto_now_add=False)
    experience = models.IntegerField()

    # Need to change it as a foreign field
    shift = models.CharField(max_length=50)

    about = models.TextField()

    def __str__(self) -> str:
        return self.user.email
