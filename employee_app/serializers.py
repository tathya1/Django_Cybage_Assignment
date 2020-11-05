from rest_framework import serializers
from employee_app.models import Department, Designation, Employee, Organization, UserProfile


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ['id', 'organizationName']


class DepartmentSerializer(serializers.ModelSerializer):

    organizationName = serializers.ReadOnlyField(
        source='organization.organizationName')

    class Meta:
        model = Department
        fields = ['id', 'departmentName', 'organizationName']


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

    '''Right way to call serializer inside a serializer, l.h.s is the 
    object on which the serailizer will get called

    department = DepartmentSerializer(many=true)'''
    class Meta:
        model = Employee
        # organization is a property defined in models.py under Employee
        fields = ['id', 'name', 'email', 'organization',
                  'department', 'designation', 'bio']

        # read_only_fields = ('organization',)
