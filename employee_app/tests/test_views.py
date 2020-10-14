from employee_app.views import DepartmentViewSet, DesignationViewSet, EmployeeViewSet
from django.test.client import RequestFactory
from employee_app.serializers import EmployeeSerializer
from rest_framework.renderers import JSONRenderer
from django.urls import reverse
from mixer.backend.django import mixer
import pytest


@pytest.mark.django_db
class Testviews:

    # testing DepartmentViewSet
    def test_department_list_display_all(self):
        mixer.blend('employee_app.Department', departmentName="HR")
        path = reverse('department-list')
        request = RequestFactory().get(path)

        response = DepartmentViewSet.as_view(actions={
            'get': 'list',
        })(request)
        assert response.status_code == 200
        assert list(response.data[0].items())[1][1] == "HR"

    def test_department_list_add_one(self):
        path = reverse('department-list')
        data = {'departmentName': 'RP'}
        request = RequestFactory().post(path, data, content_type='application/json')
        response = DepartmentViewSet.as_view(actions={
            'post': 'create',
        })(request)
        assert response.status_code == 201
        assert response.data['departmentName'] == 'RP'

    def test_department_detail_display_one(self):
        mixer.blend('employee_app.Department', departmentName="IS")
        path = reverse('department-detail', kwargs={'pk': 1})
        request = RequestFactory().get(path)
        response = DepartmentViewSet.as_view(actions={
            'get': 'retrieve',
        })(request, pk=1)
        assert response.status_code == 200
        assert response.data['departmentName'] == 'IS'

    def test_department_detail_delete_one(self):
        mixer.blend('employee_app.Department')
        path = reverse('department-detail', kwargs={'pk': 1})
        request = RequestFactory().delete(path)
        response = DepartmentViewSet.as_view(actions={
            'delete': 'destroy',
        })(request, pk=1)
        assert response.status_code == 204

    # testing DesignationViewSet

    def test_designation_list_display_all(self):
        mixer.blend('employee_app.Designation', designationName="SE")
        path = reverse('designation-list')
        request = RequestFactory().get(path)

        response = DesignationViewSet.as_view(actions={
            'get': 'list',
        })(request)
        assert response.status_code == 200
        assert list(response.data[0].items())[1][1] == "SE"

    def test_desigantion_list_add_one(self):
        path = reverse('designation-list')
        data = {'designationName': 'SSE'}
        request = RequestFactory().post(path, data, content_type='application/json')
        response = DesignationViewSet.as_view(actions={
            'post': 'create',
        })(request)
        assert response.status_code == 201
        assert response.data['designationName'] == 'SSE'

    def test_designation_detail_display_one(self):
        mixer.blend('employee_app.Designation', designationName="TA")
        path = reverse('designation-detail', kwargs={'pk': 1})
        request = RequestFactory().get(path)
        response = DesignationViewSet.as_view(actions={
            'get': 'retrieve',
        })(request, pk=1)
        assert response.status_code == 200
        assert response.data['designationName'] == 'TA'

    def test_designation_detail_delete_one(self):
        mixer.blend('employee_app.Designation')
        path = reverse('designation-detail', kwargs={'pk': 1})
        request = RequestFactory().delete(path)
        response = DesignationViewSet.as_view(actions={
            'delete': 'destroy',
        })(request, pk=1)
        assert response.status_code == 204

    # testing EmployeeViewSet

    def test_employee_list_display_all(self):
        mixer.blend('employee_app.Employee', name="Rohan")
        path = reverse('employee-list')
        request = RequestFactory().get(path)

        response = EmployeeViewSet.as_view(actions={
            'get': 'list',
        })(request)
        assert response.status_code == 200
        assert list(response.data[0].items())[1][1] == "Rohan"

    def test_employee_list_add_one(self):
        path = reverse('employee-list')
        test_emp = mixer.blend('employee_app.Employee', name="Ajay")
        emp_ser = EmployeeSerializer(test_emp)
        data = JSONRenderer().render(emp_ser.data)
        request = RequestFactory().post(path, data, content_type='application/json')
        response = EmployeeViewSet.as_view(actions={
            'post': 'create',
        })(request)
        assert response.status_code == 201
        assert response.data['name'] == 'Ajay'

    def test_employee_detail_display_one(self):
        mixer.blend('employee_app.Employee', name="Jenil")
        path = reverse('employee-detail', kwargs={'pk': 1})
        request = RequestFactory().get(path)
        response = EmployeeViewSet.as_view(actions={
            'get': 'retrieve',
        })(request, pk=1)
        assert response.status_code == 200
        assert response.data['name'] == 'Jenil'

    def test_employee_detail_delete_one(self):
        mixer.blend('employee_app.Employee')
        path = reverse('employee-detail', kwargs={'pk': 1})
        request = RequestFactory().delete(path)
        response = EmployeeViewSet.as_view(actions={
            'delete': 'destroy',
        })(request, pk=1)
        assert response.status_code == 204

#28 passed in 0.55s