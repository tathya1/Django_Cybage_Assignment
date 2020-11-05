from django.contrib import admin
from .models import Organization, Department, Designation, UserProfile, Employee
from django_reverse_admin import ReverseModelAdmin
from nested_admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline
admin.site.site_header = "Employee management system"
# from django.shortcuts import get_object_or_404

admin.site.site_header = "Employee management system"

# https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#working-with-many-to-many-models
# https://docs.djangoproject.com/en/3.1/topics/db/models/#extra-fields-on-many-to-many-relationships

# The through attribute is a reference to the model that manages the many-to-many relation. This model is automatically created by Django when you define a many-to-many field.


class MembershipInline(NestedStackedInline):
    model = Employee.department.through


class DepartmentInline(NestedStackedInline):
    model = Department
    extra = 1
    inlines = [MembershipInline]


class OrganizationAdmin(NestedModelAdmin):

    inlines = [DepartmentInline]


# class NoDefaultDeptartmentAvailable(Exception):
#     def __str__(self):
#         return "Please create default department(RP) under DefaultOrg."

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):

    model = Department


@admin.register(Employee)
class EmployeeAdmin(ReverseModelAdmin):
    fieldsets = [
        ('Personal info', {'fields': ['name']}),
        (None, {'fields': ['email']}),
        ('Profile info', {'fields': ['department']}),
        (None, {'fields': ['designation']}),
    ]

    """ departments and organization in list_display are property of Employee class,
        department in the list_filter is the field """

    list_display = ('name', 'email', 'organization',
                    'departments', 'designation', 'bio',)
    list_filter = ('department', 'designation',)

    inline_type = 'tabular'
    inline_reverse = [
        ('bio', {'fields': ['bio']}),
    ]

    # def save_model(self, request, obj, form, change):

    #     org = get_object_or_404(Organization, organizationName="DefaultOrg")
    #     dept = Department.objects.filter(departmentName="RP", organization=org)
    #     super(EmployeeAdmin, self).save_model(request, obj, form, change)
    #     if not dept:
    #         raise NoDefaultDeptartmentAvailable
    #     if not form.instance.department.all():
    #         form.cleaned_data['department'] = dept


@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    model = Designation


admin.site.register(Organization, OrganizationAdmin)
