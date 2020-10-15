from rest_framework.viewsets import ModelViewSet
from employee_app.models import Department, Designation, Employee, Organization, UserProfile
from employee_app.serializers import DepartmentSerializer, DesignationSerializer, EmployeeSerializer, OrganizationSerializer, UserProfileSerializer
#from rest_framework import permissions


class OrganizationViewSet(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    #permission_classes = [permissions.IsAuthenticated]


class DesignationViewSet(ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    #permission_classes = [permissions.IsAuthenticated]


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    #permission_classes = [permissions.IsAuthenticated]
