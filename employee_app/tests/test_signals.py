# from mixer.backend.django import mixer
# import pytest
# # from django.contrib.admin.sites import AdminSite
# # from employee_app.admin import EmployeeAdmin
# from mock import patch, MagicMock


# # class SignalsTest(TestCase):

# #     def test_save_model(self):
# #         dept = mixer.blend('employee_app.Department', departmentName="RP")
# #         emp = mixer.blend('employee_app.Employee', name="TestEmp")
# #         my_model_admin = EmployeeAdmin(model=Employee, admin_site=AdminSite())
# #         my_model_admin.save_model(obj=emp, request=None, form=None, change=None)
# #         assert my_model_admin==1

# # https://stackoverflow.com/questions/43920155/django-assert-post-save-signal-called


# @pytest.mark.django_db
# @patch('employee_app.signals.pre_delete_dept')
# def test_delete_signal(mock_signal):

#     dept = mixer.blend('employee_app.Department')
#     dept_rp = mixer.blend('employee_app.Department', departmentName= "RP")
#     dept.delete()
#     assert mock_signal.pre_delete_dept_helper().call_count == 1

    #assert mock_signal.call_count == 1

    # def test_delete_signal(self):
    #     with mock.patch('employee_app.signals.pre_delete_dept') as mocked_handler:
    #         pre_delete.connect(mocked_handler, sender=Department, dispatch_uid='set_default_department_on_delete')
    #         # do stuff that will call the post_save of User
    #     self.assertEqual(mocked_handler.call_count, 1)  # standard django
    #     # self.assert_equal(mocked_handler.call_count, 1)  # when using django-nose
