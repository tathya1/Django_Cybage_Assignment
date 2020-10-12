from django.urls import reverse, resolve

'''
> reverse('department-list')
'/employee_app/department/'

> resolve('/employee_app/department/')
ResolverMatch(func=emploee_app.views.DepartmentViewSet, args=(), kwargs={}, url_name=department-list, app_names=[], namespaces=[], route=api/department/$)

> resolve('/employee_app/department/').view_name
'department-list
'''


class TestUrls:

    # asserting employee_urls
    def test_employee_list_url(self):

        path = reverse('employee-list')
        assert resolve(path).view_name == 'employee-list'

    def test_employee_detail_url(self):

        path = reverse('employee-detail', kwargs={'pk': 1})
        assert resolve(path).view_name == 'employee-detail'

    # asserting department_urls
    def test_department_list_url(self):

        path = reverse('department-list')
        assert resolve(path).view_name == 'department-list'

    def test_department_detail_url(self):

        path = reverse('department-detail', kwargs={'pk': 1})
        assert resolve(path).view_name == 'department-detail'

    # asserting designation_urls
    def test_designation_list_url(self):

        path = reverse('designation-list')
        assert resolve(path).view_name == 'designation-list'

    def test_designation_detail_url(self):

        path = reverse('designation-detail', kwargs={'pk': 1})
        assert resolve(path).view_name == 'designation-detail'
