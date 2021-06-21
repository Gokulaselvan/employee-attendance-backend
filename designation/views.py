from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Designation, Department
from .serializers import DesignationSerializer, DepartmentSerializer


class DesignationViewsets(ModelViewSet):

    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    permission_classes = [IsAuthenticated, ]


class DepartmentViewsets(ModelViewSet):

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated, ]

    
