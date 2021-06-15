from django.urls import reverse
from django.test import TestCase

from ..forms import CustomUserCreationForm, CustomUserChangeForm


class TestUserCreationForm(TestCase):

    def test_passwords_dont_match(self) -> None:

        form = CustomUserCreationForm(data={"email": "test@gmail.com", "username": "test",
                                            "employee_id": "DT1001", "password": "wsxwsx@123",
                                            "retype_password": "wsxwsx@12"})

        self.assertEqual(
            form.errors["retype_password"], ["Your passwords must match", ])

    def test_passwords_match(self) -> None:

        form = CustomUserCreationForm(data={"email": "test@gmail.com", "username": "test",
                                            "employee_id": "DT1001", "password": "wsxwsx@123",
                                            "retype_password": "wsxwsx@123"})

        if form.is_valid():
            saved_form = form.save()
            self.assertNotEqual(saved_form.password, "wsxwsx@123")
