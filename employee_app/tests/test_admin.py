from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from employee_app.models import Organization, Department
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


class OrganizationAdminTestCase(TestCase):

    organization_form_post_payload = {
        "organizationName": "TestOrg",
        "department_set-TOTAL_FORMS": 1,
        "department_set-INITIAL_FORMS": 0,
        "department_set-MIN_NUM_FORMS": 0,
        "department_set-MAX_NUM_FORMS": 1000,
        "department_set-0-departmentName": "TestDept",
        "department_set-0-Employee_department-TOTAL_FORMS": 3,
        "department_set-0-Employee_department-INITIAL_FORMS": 0,
        "department_set-0-Employee_department-MIN_NUM_FORMS": 0,
        "department_set-0-Employee_department-MAX_NUM_FORMS": 1000
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
            dept.departmentName, self.organization_form_post_payload["department_set-0-departmentName"])
        self.assertEqual(response.status_code, 302)

    def test_organization_add_form_invalid_payload(self):
        self.client.login(
            username=self.username,
            password=self.password,
        )

        organization_form_post_payload = deepcopy(
            self.organization_form_post_payload)
        organization_form_post_payload['organizationName'] = ''

        response = self.client.post(
            reverse('admin:employee_app_organization_add'),
            organization_form_post_payload,
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
