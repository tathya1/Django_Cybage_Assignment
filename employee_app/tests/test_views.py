from employee_app.views import DepartmentViewSet, DesignationViewSet, EmployeeViewSet
from django.test.client import RequestFactory
from employee_app.serializers import EmployeeSerializer
from rest_framework.renderers import JSONRenderer
from django.urls import reverse
from mixer.backend.django import mixer
#from django.test import TestCase
import pytest

'''@classmethod
def setUpClass(cls):
    super(Testviews, cls).setUpClass()
    mixer.blend('employee_app.Department', departmentName="HR")
    mixer.blend('employee_app.Designation', designationName="SE")
    mixer.blend('employee_app.Employee', name="Tathya")
    cls.factory = RequestFactory()'''

'''we can use the fixture function as
 an input parameter of the test function, and that 
 input parameter is already the return object. 
 This behavior is called dependency injection.'''


# Creating fixtures
# The scope basically controls how often each fixture will be executed.
# five different scopes: function, class, module, package, and session.

@pytest.fixture(scope='module')
def factory():
    return RequestFactory()

# passing db fixture since not using @pytest.mark anymore
# can also parameterize the fixtures


@pytest.fixture
def dept(db):
    mixer.blend('employee_app.Department', departmentName="HR")


@pytest.fixture
def des(db):
    mixer.blend('employee_app.Designation', designationName="SE")


@pytest.fixture
def emp(db):
    return mixer.blend('employee_app.Employee', name="Tathya")

# testing DepartmentViewSet


def test_department_list_display_all(factory, dept):

    path = reverse('department-list')
    request = factory.get(path)
    response = DepartmentViewSet.as_view(actions={
        'get': 'list',
    })(request)
    assert response.status_code == 200
    assert list(response.data[0].items())[1][1] == "HR"


def test_department_list_add_one(factory, dept):

    path = reverse('department-list')
    data = {'departmentName': 'RP'}
    request = factory.post(path, data, content_type='application/json')
    response = DepartmentViewSet.as_view(actions={
        'post': 'create',
    })(request)
    assert response.status_code == 201
    assert response.data['departmentName'] == 'RP'


def test_department_detail_display_one(factory, dept):

    path = reverse('department-detail', kwargs={'pk': 1})
    request = factory.get(path)
    response = DepartmentViewSet.as_view(actions={
        'get': 'retrieve',
    })(request, pk=1)
    assert response.status_code == 200
    assert response.data['departmentName'] == 'HR'


def test_department_detail_delete_one(factory, dept):

    path = reverse('department-detail', kwargs={'pk': 1})
    request = factory.delete(path)
    response = DepartmentViewSet.as_view(actions={
        'delete': 'destroy',
    })(request, pk=1)
    assert response.status_code == 204


# testing DesignationViewSet
def test_designation_list_display_all(factory, des):

    path = reverse('designation-list')
    request = factory.get(path)
    response = DesignationViewSet.as_view(actions={
        'get': 'list',
    })(request)
    assert response.status_code == 200
    assert list(response.data[0].items())[1][1] == "SE"


def test_desigantion_list_add_one(factory, des):
    path = reverse('designation-list')
    data = {'designationName': 'SSE'}
    request = factory.post(path, data, content_type='application/json')
    response = DesignationViewSet.as_view(actions={
        'post': 'create',
    })(request)
    assert response.status_code == 201
    assert response.data['designationName'] == 'SSE'


def test_designation_detail_display_one(factory, des):

    path = reverse('designation-detail', kwargs={'pk': 1})
    request = factory.get(path)
    response = DesignationViewSet.as_view(actions={
        'get': 'retrieve',
    })(request, pk=1)
    assert response.status_code == 200
    assert response.data['designationName'] == 'SE'


def test_designation_detail_delete_one(factory, des):

    path = reverse('designation-detail', kwargs={'pk': 1})
    request = factory.delete(path)
    response = DesignationViewSet.as_view(actions={
        'delete': 'destroy',
    })(request, pk=1)
    assert response.status_code == 204

# testing EmployeeViewSet


def test_employee_list_display_all(factory, emp):

    path = reverse('employee-list')
    request = factory.get(path)
    response = EmployeeViewSet.as_view(actions={
        'get': 'list',
    })(request)
    assert response.status_code == 200
    assert list(response.data[0].items())[1][1] == "Tathya"


def test_employee_list_add_one(factory, emp):

    path = reverse('employee-list')
    emp_ser = EmployeeSerializer(emp)
    data = JSONRenderer().render(emp_ser.data)
    request = factory.post(path, data, content_type='application/json')
    response = EmployeeViewSet.as_view(actions={
        'post': 'create',
    })(request)
    assert response.status_code == 201
    assert response.data['name'] == 'Tathya'


def test_employee_detail_display_one(factory, emp):

    path = reverse('employee-detail', kwargs={'pk': 1})
    request = factory.get(path)
    response = EmployeeViewSet.as_view(actions={
        'get': 'retrieve',
    })(request, pk=1)
    assert response.status_code == 200
    assert response.data['name'] == 'Tathya'


def test_employee_detail_delete_one(factory, emp):

    path = reverse('employee-detail', kwargs={'pk': 1})
    request = factory.delete(path)
    response = EmployeeViewSet.as_view(actions={
        'delete': 'destroy',
    })(request, pk=1)
    assert response.status_code == 204
