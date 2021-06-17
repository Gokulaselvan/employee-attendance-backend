from django.test import TestCase

from .models import Designation, Department


class TestDesignation(TestCase):

    def test_str_repr(self) -> None:
        """Checks for the str method"""

        designation = Designation.objects.create(
            designation_name="Product Manager")

        self.assertEqual(str(designation), "Product Manager")


class TestDepartment(TestCase):

    def test_str_repr(self) -> None:
        """Checks for the str method"""

        department = Department.objects.create(department_name="Development")

        self.assertEqual(str(department), "Development")
