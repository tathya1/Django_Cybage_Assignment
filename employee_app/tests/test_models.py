from mixer.backend.django import mixer
from employee_app.models import Department, Designation
import pytest

# The __str__() method is called whenever you call str() on an object

# creating fixtures


@pytest.fixture
def dept(db):
    return mixer.blend('employee_app.Department', departmentName='HR')


@pytest.fixture
def dept1(db):
    return mixer.blend('employee_app.Department', departmentName='IS')


@pytest.fixture
def des(db):
    return mixer.blend('employee_app.Designation', desigantionName='SE')


@pytest.fixture
def emp(db):
    return mixer.blend('employee_app.Employee', name='Tathya')

@pytest.fixture
def org(db):
    return mixer.blend('employee_app.Organization', organizationName='Cybage')

@pytest.fixture
def bio(db):
    return mixer.blend('employee_app.UserProfile', bio='Hey')

# asserting __str__ for userprofile
def test__str__equals_bio(bio):

    assert str(bio) == bio.bio


def test__str__not_equals_bio(bio):

    assert str(bio) != 'Bye'

# asserting __str__ for organization
def test__str__equals_organizationName(org):

    assert str(org) == org.organizationName


def test__str__not_equals_organizationName(org):

    assert str(org) != 'Infy'

# asserting __str__ for department
def test__str__equals_departmentName(dept):

    assert str(dept) == dept.departmentName


def test__str__not_equals_departmentName(dept):

    assert str(dept) != 'IS'


# asserting __str__ for designation
def test__str__equals_desigantionName(des):

    assert str(des) == des.designationName


def test__str__not_equals_desigantionName(des):

    assert str(des) != 'SSE'


# asserting __str__ for employee
def test__str__equals_employeeName(emp):

    assert str(emp) == emp.name


def test__str__not_equals_employeeName(emp):

    assert str(emp) != 'Steve'


# asserting Employee.departments()
def test_departments_returns_nonempty_list(dept):

    employee = mixer.blend('employee_app.Employee', department=[dept])
    assert employee.departments()


def test_departments_returns_empty_list(emp):

    # emp fixture has no depatments given
    assert not emp.departments()


def test_departments_returns_same_count(dept, dept1):

    employee = mixer.blend('employee_app.Employee', department=[dept, dept1])
    # employee.departments() returns a str of depts sepated by ','
    assert (employee.departments().count(',')+1) == 2


def test_departments_returns_different_count(dept, dept1):

    employee = mixer.blend('employee_app.Employee', department=[dept, dept1])
    assert not (employee.departments().count(',')+1) == 3
