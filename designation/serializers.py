from django.db import models
from rest_framework import fields, serializers

from .models import Designation, Department

class DesignationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Designation
        fields = "__all__"
        

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = "__all__"