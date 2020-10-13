from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from employee_app.models import Department, Designation, Employee
from employee_app.serializers import DepartmentSerializer, DesignationSerializer, EmployeeSerializer
from rest_framework import permissions

class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class DesignationViewSet(ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    permission_classes = [permissions.IsAuthenticated]


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
