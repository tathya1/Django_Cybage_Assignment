from rest_framework import serializers
from employee_app.models import Department, Designation, Employee, Organization, UserProfile


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ['id', 'organizationName']


class DepartmentSerializer(serializers.ModelSerializer):
    organization = serializers.SlugRelatedField(
        slug_field='organizationName', queryset=Organization.objects.all())

    class Meta:
        model = Department
        fields = ['id', 'departmentName', 'organization']


class DesignationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Designation
        fields = ['id', 'designationName']


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['id', 'bio']


class EmployeeSerializer(serializers.ModelSerializer):

    department = serializers.SlugRelatedField(
        slug_field='departmentName', queryset=Department.objects.all(), many=True)
    designation = serializers.SlugRelatedField(
        slug_field='designationName', queryset=Designation.objects.all())
    bio = serializers.SlugRelatedField(
        slug_field='bio', queryset=UserProfile.objects.all())

    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'department', 'designation', 'bio']
