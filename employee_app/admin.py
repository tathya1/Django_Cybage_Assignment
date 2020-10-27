from django.contrib import admin
from .models import Organization, Department, Designation, UserProfile, Employee
from django_reverse_admin import ReverseModelAdmin
from nested_admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver
admin.site.site_header = "Employee management system"

# https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#working-with-many-to-many-models
# The through attribute is a reference to the model that manages the many-to-many relation. This model is automatically created by Django when you define a many-to-many field.

class MembershipInline(NestedStackedInline):
    model = Employee.department.through


class DepartmentInline(NestedStackedInline):
    model = Department
    extra = 1
    inlines = [MembershipInline]


class OrganizationAdmin(NestedModelAdmin):

    inlines = [DepartmentInline]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):

    @receiver(pre_delete, sender=Department, dispatch_uid='set_default_department_on_delete')
    def pre_delete_dept(sender, instance, *args, **kwargs):
        emps = instance.emp.all()
        if not Department.objects.filter(departmentName="RP"):
            dept = Department.objects.create(
                departmentName="RP", organization=instance.organization)
        else:
            dept = Department.objects.get(departmentName="RP")

        for emp in emps:
            if emp.department.count()==1:
                emp.department.add(dept)
                emp.save()

# Reverse admin


@admin.register(Employee)
class EmployeeAdmin(ReverseModelAdmin):
    fieldsets = [
        ('Personal info', {'fields': ['name']}),
        (None, {'fields': ['email']}),
        ('Profile info', {'fields': ['department']}),
        (None, {'fields': ['designation']}),
    ]

    """ departments in list_display is the method of Employee class,
        department in the list_filter is the field """

    list_display = ('name', 'email', 'departments', 'designation', 'bio')
    list_filter = ('designation', 'department')

    inline_type = 'tabular'
    inline_reverse = [
        ('bio', {'fields': ['bio']}),
    ]
    
    # @receiver(post_save, sender=Employee, dispatch_uid='set_default_department_on_creation')
    # def post_save_dept(sender, instance, *args, **kwargs):
    #     dept = Department.objects.all()[0]
    #     c = instance.departments()
    #     print(c)
    #     if instance.department.count()==0:

    #       instance.department.add(dept)
    #       instance.save()


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Designation)
