from django.urls import reverse
from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class TestUserCustomManager(TestCase):

    def test_str_repr(self) -> None:
        """Checks for the Str method"""

        new_user_str = User.objects.create_superuser(email="test@gmail.com",
                                                     username="test", employee_id="DT1001", password="wsxwsx@123")

        self.assertEqual(str(new_user_str), "test@gmail.com")

    def test_can_create_super_user(self) -> None:
        """Checks for the usage of create superuser"""

        new_user = User.objects.create_superuser(email="test@gmail.com",
                                                 username="test", employee_id="DT1001", password="wsxwsx@123")

        self.assertTrue(new_user.is_admin)
        self.assertTrue(new_user.is_superuser)
        self.assertTrue(new_user.is_active)
        self.assertTrue(new_user.is_staff)

    def test_cant_create_super_user(self) -> None:
        """Checks for the create superuser cant be created without required arguments"""

        with self.assertRaises(TypeError):
            User.objects.create_superuser()

    def test_can_create_user(self) -> None:
        """Checks can create user"""

        n_user = User.objects.create_user(email="test@gmail.com",
                                          username="test", employee_id="DT1001", password="wsxwsx@123")

        self.assertFalse(n_user.is_admin)
        self.assertFalse(n_user.is_superuser)
        self.assertTrue(n_user.is_active)
        self.assertFalse(n_user.is_staff)

    def test_cant_create_user(self) -> None:
        """Checks user cant be created without these arguments"""

        with self.assertRaises(TypeError):
            User.objects.create_user(
                email="test@gmail.com", employee_id="DT1001", password="wsxwsx@123")

        with self.assertRaises(TypeError):
            User.objects.create_user(
                username="test", employee_id="DT1001", password="wsxwsx@123")

        with self.assertRaises(TypeError):
            User.objects.create_user(email="test@gmail.com",
                                     username="test", password="wsxwsx@123")

        with self.assertRaises(TypeError):
            User.objects.create_user(email="test@gmail.com",
                                     username="test", employee_id="DT1001")
