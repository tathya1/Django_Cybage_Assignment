from rest_framework.viewsets import ModelViewSet
from employee_app.models import Department, Designation, Employee, Organization, UserProfile
from employee_app import serializers
#from rest_framework import permissions


class OrganizationViewSet(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer


class DepartmentViewSet(ModelViewSet):
    serializer_class = serializers.DepartmentSerializer

    def get_queryset(self):
        return Department.objects.filter(organization=self.kwargs['organization_pk'])

    # https://github.com/alanjds/drf-nested-routers/issues/187

    def perform_create(self, serializer):
        org = Organization.objects.filter(
            id=self.kwargs['organization_pk']).first()
        serializer.save(organization=org)

    #permission_classes = [permissions.IsAuthenticated]


class DesignationViewSet(ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = serializers.DesignationSerializer
    #permission_classes = [permissions.IsAuthenticated]


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    #permission_classes = [permissions.IsAuthenticated]
