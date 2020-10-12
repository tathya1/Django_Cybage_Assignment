from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from employee_app.models import Department, Designation, Employee
from employee_app.serializers import DepartmentSerializer, DesignationSerializer, EmployeeSerializer


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DesignationViewSet(ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
