from django.test.client import RequestFactory
from employee_app import serializers
from mixer.backend.django import mixer
from rest_framework.renderers import JSONRenderer
from employee_app.models import Department, Organization, Designation, UserProfile, Employee
import pytest


@pytest.fixture
def org(db):
    return Organization.objects.create(organizationName="INFY")


@pytest.fixture
def des(db):
    return Designation.objects.create(designationName="SE")


@pytest.fixture
def bio(db):
    return UserProfile.objects.create(bio="Hey")


@pytest.fixture
def dept(db):
    return Department.objects.create(departmentName='IS')

# Testing OrganizationSerializer


def test_organization_serializer(org):
    org_ser = serializers.OrganizationSerializer(org)
    assert org_ser.data['organizationName'] == org.organizationName


def test_organization_de_serializer(db):
    data = {'organizationName': 'Cybage'}
    org_ser = serializers.OrganizationSerializer(data=data)
    org_ser.is_valid()
    org_ser.save()
    assert org_ser.data['organizationName'] == data['organizationName']

# Testing DepartmentSerializer


def test_department_serializer(org):
    dept = Department.objects.create(departmentName='RP', organization=org)
    dept_ser = serializers.DepartmentSerializer(dept)
    assert dept_ser.data['departmentName'] == dept.departmentName


def test_department_de_serializer(db, org):
    data = {'departmentName': 'RP', 'organization': 'INFY'}
    dept_ser = serializers.DepartmentSerializer(data=data)
    # print(dept_ser.is_valid())
    # print(dept_ser.errors)
    dept_ser.is_valid()
    dept_ser.save()
    assert dept_ser.data['departmentName'] == data['departmentName']

# Testing DesignationSerializer


def test_designation_serializer(des):
    des_ser = serializers.DesignationSerializer(des)
    assert des_ser.data['designationName'] == des.designationName


def test_designation_de_serializer(db):
    data = {'designationName': 'SE'}
    des_ser = serializers.DesignationSerializer(data=data)
    des_ser.is_valid()
    des_ser.save()
    assert des_ser.data['designationName'] == data['designationName']

# Testing UserProfileSerializer


def test_userprofile_serializer(bio):
    up_ser = serializers.UserProfileSerializer(bio)
    assert up_ser.data['bio'] == bio.bio


def test_userprofile_de_serializer(db):
    data = {'bio': 'Hey'}
    up_ser = serializers.UserProfileSerializer(data=data)
    up_ser.is_valid()
    up_ser.save()
    assert up_ser.data['bio'] == data['bio']

# Testing EmployeeSerializer


def test_employee_serializer(org, des, bio):
    dept = Department.objects.create(departmentName='RP', organization=org)
    emp = Employee.objects.create(
        name='Alex', email='alex@hotmail.com', designation=des, bio=bio)
    emp.department.add(dept)
    emp_ser = serializers.EmployeeSerializer(emp)
    assert emp_ser.data['name'] == emp.name


def test_employee_de_serializer(db, dept, des, bio):
    data = {'name': 'Tathya', 'email': 'tathya@hotmail.com',
            'department': ['IS'], 'designation': 'SE', 'bio': 'Hey'}
    emp_ser = serializers.EmployeeSerializer(data=data)
    print(emp_ser.is_valid())
    print(emp_ser.errors)
    emp_ser.is_valid()
    emp_ser.save()
    assert emp_ser.data['name'] == data['name']
