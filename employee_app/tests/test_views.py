from employee_app.models import Employee, Department, Designation
from django.contrib.auth.models import User
from django.test.client import RequestFactory
from rest_framework.test import APIRequestFactory
from django.urls import reverse
from mixer.backend.django import mixer
from rest_framework.test import APITestCase
from employee_app.views import DepartmentViewSet
import pytest

'''Testviews inherting Middleware gives this warning
cannot collect test class 'Testviews' because it has a __init__ constructor'''

@pytest.mark.django_db
class Testviews(APITestCase):

    #Testing department views
    def test_department_list_view_get(self):
        path = reverse('department-list')
        response = self.client.get(path)
        assert response.status_code == 200

    def test_department_list_view_post(self):
        path = reverse('department-list')
        data = {'departmentName':'HR'}
        response = self.client.post(path, data, format='json')
        assert response.status_code == 201
    
    def test_department_list_view_post_same_data(self):
        path = reverse('department-list')
        data = {'departmentName':'HR'}
        response = self.client.post(path, data, format='json')
        assert response.data['departmentName'] == "HR"
    
    def test_department_list_view_post_different_data(self):
        path = reverse('department-list')
        data = {'departmentName':'HR'}
        response = self.client.post(path, data, format='json')
        assert not response.data['departmentName'] == "IS"

