from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, UserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, employee_id, password=None):
        if not username:
            raise ValueError("Users must have an username")
        if not email:
            raise ValueError("Users must have an Email Address")
        if not employee_id:
            raise ValueError("Users must have an Employee ID")
        if not password:
            raise ValueError("Users must have a Password")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            employee_id=employee_id
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, employee_id, password):

        user = self.create_user(
            email=email, username=username,
            employee_id=employee_id, password=password)

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    employee_id = models.CharField(max_length=24, unique=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'employee_id']

    objects = UserManager()

    def __str__(self) -> str:
        return self.email
