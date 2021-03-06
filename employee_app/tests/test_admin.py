from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from employee_app.models import Organization, Department, Employee, Designation, UserProfile
from copy import deepcopy


def _create_super_user():
    username = 'admin'
    password = User.objects.make_random_password()

    user = User.objects.create_superuser(
        email='admin@admin.com',
        password=password,
        username=username,
    )

    return (username, password)


class OrganizationAdminTest(TestCase):

    organization_form_post_payload = {

        "organizationName": "TestOrg",
        "dept-TOTAL_FORMS": 1,
        "dept-INITIAL_FORMS": 0,
        "dept-MIN_NUM_FORMS": 0,
        "dept-MAX_NUM_FORMS": 1000,
        "dept-0-departmentName": "TestDept",
        "dept-0-Employee_department-TOTAL_FORMS": 3,
        "dept-0-Employee_department-INITIAL_FORMS": 0,
        "dept-0-Employee_department-MIN_NUM_FORMS": 0,
        "dept-0-Employee_department-MAX_NUM_FORMS": 1000,
        "dept-empty-Employee_department-TOTAL_FORMS": 3,
        "dept-empty-Employee_department-INITIAL_FORMS": 0,
        "dept-empty-Employee_department-MIN_NUM_FORMS": 0,
        "dept-empty-Employee_department-MAX_NUM_FORMS": 1000,
    }

    def setUp(self):
        (self.username, self.password) = _create_super_user()

        org = Organization.objects.create(organizationName='Org1')
        self.org_id = org.id

    def test_load_organization_detail_form(self):
        self.client.login(
            username=self.username,
            password=self.password,
        )

        response = self.client.get(
            reverse(
                'admin:employee_app_organization_change',
                args=(self.org_id,),
            )
        )
        org = Organization.objects.get(id=self.org_id)

        self.assertContains(response, org.organizationName)
        self.assertEqual(response.status_code, 200)

    def test_organization_add_form_valid_payload(self):
        self.client.login(
            username=self.username,
            password=self.password,
        )

        response = self.client.post(
            reverse('admin:employee_app_organization_add'),
            self.organization_form_post_payload,
        )

        org = Organization.objects.get(
            organizationName=self.organization_form_post_payload["organizationName"])
        dept = Department.objects.get(organization=org)

        self.assertEqual(org.organizationName,
                         self.organization_form_post_payload["organizationName"])
        self.assertEqual(
            dept.departmentName, self.organization_form_post_payload["dept-0-departmentName"])
        self.assertEqual(response.status_code, 302)

    def test_organization_add_form_invalid_payload(self):
        self.client.login(
            username=self.username,
            password=self.password,
        )

        organization_form_post_invalid_payload = deepcopy(
            self.organization_form_post_payload)
        organization_form_post_invalid_payload['organizationName'] = ''

        response = self.client.post(
            reverse('admin:employee_app_organization_add'),
            organization_form_post_invalid_payload,
        )

        self.assertContains(response, 'Please correct the error below.')
        self.assertEqual(response.status_code, 200)

    def test_organization_change_form(self):
        self.client.login(
            username=self.username,
            password=self.password,
        )

        # copy of payload
        organization_form_post_payload = deepcopy(
            self.organization_form_post_payload)
        organization_form_post_payload['organizationName'] = 'TestOrgNew'

        response = self.client.post(
            reverse(
                'admin:employee_app_organization_change',
                args=(self.org_id,),
            ),
            organization_form_post_payload
        )
        org = Organization.objects.get(id=self.org_id)

        self.assertEqual(org.organizationName,
                         organization_form_post_payload['organizationName'])
        self.assertEqual(response.status_code, 302)

    def test_organization_delete(self):
        self.client.login(
            username=self.username,
            password=self.password,
        )

        are_you_sure = {"post": "yes"}

        response = self.client.post(
            reverse(
                'admin:employee_app_organization_delete',
                args=(self.org_id,),
            ),
            are_you_sure
        )

        # get throws an exception if not found, filter dosen't
        deletedOrg = Organization.objects.filter(pk=self.org_id).first()
        self.assertEqual(deletedOrg, None)
        self.assertEqual(response.status_code, 302)


class EmployeeAdminTest(TestCase):

    employee_form_post_payload = {
        "name": "TestUser",
        "email": "test@test.com",
        "form-TOTAL_FORMS": 1,
        "form-INITIAL_FORMS": 0,
        "form-MIN_NUM_FORMS": 0,
        "form-MAX_NUM_FORMS": 1,
        "form-0-bio": "hey django"
    }

    def setUp(self):
        (self.username, self.password) = _create_super_user()
        des = Designation.objects.create(designationName='TestDes')
        bio = UserProfile.objects.create(bio='TestBio')
        org = Organization.objects.create(organizationName="TestOrg")
        dept = Department.objects.create(departmentName="RP",organization=org)
        emp = Employee.objects.create(name='TestEmp', designation=des, bio=bio)
        emp.department.add(dept)
        self.emp_id = emp.id

        self.employee_form_post_payload['designation'] = des.pk
        self.employee_form_post_payload['department'] = dept.pk

    def test_load_employee_detail_form(self):
        self.client.login(
            username=self.username,
            password=self.password,
        )

        response = self.client.get(
            reverse(
                'admin:employee_app_employee_change',
                args=(self.emp_id,),
            )
        )
        emp = Employee.objects.get(id=self.emp_id)

        self.assertContains(response, emp.name)
        self.assertEqual(response.status_code, 200)

    def test_employee_add_form_valid_payload(self):
        self.client.login(
            username=self.username,
            password=self.password,
        )

        response = self.client.post(
            reverse('admin:employee_app_employee_add'),
            self.employee_form_post_payload,
        )
        print(response)
        emp = Employee.objects.get(
            name=self.employee_form_post_payload["name"])
        self.assertEqual(emp.name, self.employee_form_post_payload["name"])
        self.assertEqual(response.status_code, 302)

    def test_employee_add_form_in_valid_payload(self):
        self.client.login(
            username=self.username,
            password=self.password,
        )

        employee_form_post_invalid_payload = deepcopy(
            self.employee_form_post_payload)
        employee_form_post_invalid_payload['name'] = ''

        response = self.client.post(
            reverse('admin:employee_app_employee_add'),
            employee_form_post_invalid_payload,
        )

        self.assertContains(response, 'This field is required.')
        self.assertEqual(response.status_code, 200)

    def test_employee_change_form(self):
        self.client.login(
            username=self.username,
            password=self.password,
        )

        employee_form_post_payload = deepcopy(
            self.employee_form_post_payload)
        employee_form_post_payload['name'] = 'TestEmpNew'

        response = self.client.post(
            reverse(
                'admin:employee_app_employee_change',
                args=(self.emp_id,),
            ),
            employee_form_post_payload
        )
        emp = Employee.objects.get(id=self.emp_id)

        self.assertEqual(emp.name,
                         employee_form_post_payload['name'])
        self.assertEqual(response.status_code, 302)

    def test_employee_delete(self):
        self.client.login(
            username=self.username,
            password=self.password,
        )

        are_you_sure = {"post": "yes"}

        response = self.client.post(
            reverse(
                'admin:employee_app_employee_delete',
                args=(self.emp_id,),
            ),
            are_you_sure
        )

        deletedEmp = Employee.objects.filter(pk=self.emp_id).first()
        self.assertEqual(deletedEmp, None)
        self.assertEqual(response.status_code, 302)


class DesignationAdminTest(TestCase):

    designation_form_post_payload = {
        "designationName": "TestHR"
    }

    def setUp(self):
        (self.username, self.password) = _create_super_user()

        des = Designation.objects.create(designationName='TestDes')
        self.des_id = des.id

    def test_load_designation_detail_form(self):
        self.client.login(
            username=self.username,
            password=self.password,
        )

        response = self.client.get(
            reverse(
                'admin:employee_app_designation_change',
                args=(self.des_id,),
            )
        )
        des = Designation.objects.get(id=self.des_id)

        self.assertContains(response, des.designationName)
        self.assertEqual(response.status_code, 200)

    def test_designation_add_form_valid_payload(self):
        self.client.login(
            username=self.username,
            password=self.password,
        )

        response = self.client.post(
            reverse('admin:employee_app_designation_add'),
            self.designation_form_post_payload,
        )

        des = Designation.objects.get(
            designationName=self.designation_form_post_payload["designationName"])

        self.assertEqual(des.designationName,
                         self.designation_form_post_payload["designationName"])
        self.assertEqual(response.status_code, 302)

    def test_designation_add_form_invalid_payload(self):
        self.client.login(
            username=self.username,
            password=self.password,
        )

        designation_form_post_payload = deepcopy(
            self.designation_form_post_payload)
        designation_form_post_payload['designationName'] = ''

        response = self.client.post(
            reverse('admin:employee_app_designation_add'),
            designation_form_post_payload,
        )

        self.assertContains(response, 'Please correct the error below.')
        self.assertEqual(response.status_code, 200)

    def test_designation_change_form(self):
        self.client.login(
            username=self.username,
            password=self.password,
        )

        designation_form_post_payload = deepcopy(
            self.designation_form_post_payload)
        designation_form_post_payload['designationName'] = 'NewTestOrg'

        response = self.client.post(
            reverse(
                'admin:employee_app_designation_change',
                args=(self.des_id,),
            ),
            designation_form_post_payload
        )
        des = Designation.objects.get(id=self.des_id)

        self.assertEqual(des.designationName,
                         designation_form_post_payload['designationName'])
        self.assertEqual(response.status_code, 302)

    def test_designation_delete(self):
        self.client.login(
            username=self.username,
            password=self.password,
        )

        are_you_sure = {"post": "yes"}

        response = self.client.post(
            reverse(
                'admin:employee_app_designation_delete',
                args=(self.des_id,),
            ),
            are_you_sure
        )

        deletedDes = Designation.objects.filter(pk=self.des_id).first()
        self.assertEqual(deletedDes, None)
        self.assertEqual(response.status_code, 302)


class DepartmentAdminTest(TestCase):

    department_form_post_payload = {
        "departmentName": "TestDept",

    }

    def setUp(self):
        (self.username, self.password) = _create_super_user()

        org = Organization.objects.create(organizationName='TestOrg')
        dept = Department.objects.create(
            departmentName='TestDeptNew', organization=org)
        self.dept_id = dept.id

        self.department_form_post_payload['organization'] = org.pk

    def test_load_department_detail_form(self):
        self.client.login(
            username=self.username,
            password=self.password,
        )

        response = self.client.get(
            reverse(
                'admin:employee_app_department_change',
                args=(self.dept_id,),
            )
        )
        dept = Department.objects.get(id=self.dept_id)

        self.assertContains(response, dept.departmentName)
        self.assertEqual(response.status_code, 200)

    def test_department_add_form_valid_payload(self):
        self.client.login(
            username=self.username,
            password=self.password,
        )

        response = self.client.post(
            reverse('admin:employee_app_department_add'),
            self.department_form_post_payload,
        )

        dept = Department.objects.get(
            departmentName=self.department_form_post_payload["departmentName"])

        self.assertEqual(dept.departmentName,
                         self.department_form_post_payload["departmentName"])
        self.assertEqual(response.status_code, 302)

    def test_department_add_form_invalid_payload(self):
        self.client.login(
            username=self.username,
            password=self.password,
        )

        department_form_post_payload = deepcopy(
            self.department_form_post_payload)
        department_form_post_payload['departmentName'] = ''

        response = self.client.post(
            reverse('admin:employee_app_department_add'),
            department_form_post_payload,
        )

        self.assertContains(response, 'Please correct the error below.')
        self.assertEqual(response.status_code, 200)

    def test_department_change_form(self):
        self.client.login(
            username=self.username,
            password=self.password,
        )

        department_form_post_payload = deepcopy(
            self.department_form_post_payload)
        department_form_post_payload['departmentName'] = 'NewTestOrg'

        response = self.client.post(
            reverse(
                'admin:employee_app_department_change',
                args=(self.dept_id,),
            ),
            department_form_post_payload
        )
        dept = Department.objects.get(id=self.dept_id)

        self.assertEqual(dept.departmentName,
                         department_form_post_payload['departmentName'])
        self.assertEqual(response.status_code, 302)

    def test_department_delete(self):
        self.client.login(
            username=self.username,
            password=self.password,
        )

        are_you_sure = {"post": "yes"}

        response = self.client.post(
            reverse(
                'admin:employee_app_department_delete',
                args=(self.dept_id,),
            ),
            are_you_sure
        )

        deletedDes = Department.objects.filter(pk=self.dept_id).first()
        self.assertEqual(deletedDes, None)
        self.assertEqual(response.status_code, 302)
