from mixer.backend.django import mixer
from employee_app.models import Department, Designation
import pytest

# The __str__() method is called whenever you call str() on an object


@pytest.mark.django_db
class TestModels:

    # asserting __str__ for department

    def test__str__equals_departmentName(self):

        #mixer.blend('employee_app.Department', departmentName='HR')
        department = Department(departmentName='HR')
        assert str(department) == department.departmentName

    def test__str__not_equals_departmentName(self):

        department = Department(departmentName='HR')
        assert str(department) != 'IS'

    # asserting __str__ for designation

    def test__str__equals_desigantionName(self):

        #mixer.blend('employee_app.Designation', desigantionName='SE')
        desigantion = Designation(designationName='SE')
        assert str(desigantion) == desigantion.designationName

    def test__str__not_equals_desigantionName(self):

        desigantion = Designation(designationName='SE')
        assert str(desigantion) != 'SSE'

    # asserting __str__ for employee

    def test__str__equals_employeeName(self):

        employee = mixer.blend('employee_app.Employee', name='Tathya')
        assert str(employee) == employee.name

    def test__str__not_equals_employeeName(self):

        employee = mixer.blend('employee_app.Employee', name='Tathya')
        assert str(employee) != 'Steve'

    # asserting Employee.departments()

    def test_departments_returns_nonempty_list(self):

        d = mixer.blend('employee_app.Department', departmentName='HR')
        employee = mixer.blend('employee_app.Employee', department=[d])
        assert employee.departments()

    def test_departments_returns_empty_list(self):

        employee = mixer.blend('employee_app.Employee')
        assert not employee.departments()

    def test_departments_returns_same_count(self):

        d1 = mixer.blend('employee_app.Department', departmentName='HR')
        d2 = mixer.blend('employee_app.Department', departmentName='IS')
        employee = mixer.blend('employee_app.Employee', department=[d1, d2])
        assert (employee.departments().count(',')+1) == 2

    def test_departments_returns_different_count(self):

        d1 = mixer.blend('employee_app.Department', departmentName='HR')
        d2 = mixer.blend('employee_app.Department', departmentName='IS')
        employee = mixer.blend('employee_app.Employee', department=[d1, d2])
        assert not (employee.departments().count(',')+1) == 3
