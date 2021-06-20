from django.db import models


class Shift(models.Model):

    shift_name = models.CharField(max_length=50)
    shift_timing_start = models.TimeField(auto_now=False, auto_now_add=False)
    shift_timing_end = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):

        return self.shift_name
