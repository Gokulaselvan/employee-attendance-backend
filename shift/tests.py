from django.test import TestCase
import datetime

from .models import Shift


class TestShift(TestCase):

    def test_str_repr(self) -> None:

        shift = Shift.objects.create(
            shift_name="General",
            shift_timing_start=datetime.time(9, 00, 00),
            shift_timing_end=datetime.time(5, 30, 00),
        )
        self.assertEqual(str(shift), "General")
