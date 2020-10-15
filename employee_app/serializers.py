from rest_framework import serializers
from employee_app.models import Department, Designation, Employee


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ['id', 'departmentName']


class DesignationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Designation
        fields = ['id', 'designationName']


class EmployeeSerializer(serializers.ModelSerializer):

    department = serializers.SlugRelatedField(slug_field='departmentName', queryset=Department.objects.all(), many=True) 
    designation = serializers.SlugRelatedField(slug_field='designationName', queryset=Designation.objects.all())

    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'department', 'designation']
