from django.db import models

class Designation(models.Model):

    designation_name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.designation_name

class Department(models.Model):

    department_name = models.CharField(max_length=64)

    def __str__(self):
        return self.department_name
    