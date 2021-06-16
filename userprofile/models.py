from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth import get_user_model

from django.core.validators import MaxValueValidator

User = get_user_model()


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Need to change it as foreign key field
    designation = models.CharField(max_length=50)

    # Need to change it as foreign key field
    department = models.CharField(max_length=50)
    # Need to add Profile picture field

    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    joining_date = models.DateField(auto_now=False, auto_now_add=False)

    experience = models.PositiveIntegerField(
        default=0, validators=[MaxValueValidator(limit_value=99)])

    # Need to change it as a foreign field
    shift = models.CharField(max_length=50)

    about = models.TextField(max_length=254)

    def __str__(self) -> str:
        return self.user.email

    def clean(self) -> None:
        if self.date_of_birth > self.joining_date:
            raise ValidationError(
                "Date Of Birth must be lesser than the Joining Date")
        return super().clean()
