from django.test import TestCase

from .models import Designation


class TestDesignation(TestCase):

    def test_str_repr(self) -> None:
        """Checks for the str method"""

        designation = Designation.objects.create(designation_name = "Product Manager")

        self.assertEqual(str(designation), "Product Manager")
