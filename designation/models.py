from django.db import models

class Designation(models.Model):

    designation_name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.designation_name