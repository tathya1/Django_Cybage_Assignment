from django.contrib import admin
from .models import Organization, Department, Designation, UserProfile, Employee
from django_reverse_admin import ReverseModelAdmin


class EmployeeInline(admin.StackedInline):
    model = Employee
    extra = 1


class DesignationAdmin(admin.ModelAdmin):

    inlines = [EmployeeInline]


class DepartmentInline(admin.StackedInline):
    model = Department
    extra = 3


class OrganizationAdmin(admin.ModelAdmin):

    inlines = [DepartmentInline]

# Reverse admin


class EmployeeAdmin(ReverseModelAdmin):
    fieldsets = [
        ('Personal info', {'fields': ['name']}),
        (None, {'fields': ['email']}),
        ('Profile info', {'fields': ['department']}),
        (None, {'fields': ['designation']}),
    ]

    """ departments in list_display is the method of Employee class,
        department in the list_filter is the field"""

    list_display = ('name', 'email', 'departments', 'designation', 'bio')
    list_filter = ('designation', 'department', 'bio')

    inline_type = 'tabular'
    inline_reverse = ['department',
                      ('bio', {'fields': ['bio']}),
                      ]


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Department)
admin.site.register(Designation, DesignationAdmin)
admin.site.register(UserProfile)
admin.site.register(Employee, EmployeeAdmin)
