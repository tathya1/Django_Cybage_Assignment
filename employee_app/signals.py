from django.db.models.signals import pre_delete, post_save, post_delete, pre_save, m2m_changed
from django.dispatch import receiver
from employee_app.models import Organization, Department, Designation, UserProfile, Employee
#from django.db import transaction

@receiver(pre_delete, sender=Department, dispatch_uid='set_default_department_on_delete')
def pre_delete_dept(sender, instance, *args, **kwargs):
    emps = instance.emp.all()

    if not Department.objects.filter(departmentName="RP"):
        dept = Department.objects.create(
            departmentName="RP", organization=instance.organization)
    else:
        dept = Department.objects.get(departmentName="RP")

    for emp in emps:
        if emp.department.count() == 1:
            emp.department.add(dept)
            emp.save()

@receiver(post_delete, sender=Employee, dispatch_uid='delete_userprofile_on_emp_deletion')
def delete_user_profile(sender, instance, *args, **kwargs):
    userprofile = instance.bio
    userprofile.delete()



