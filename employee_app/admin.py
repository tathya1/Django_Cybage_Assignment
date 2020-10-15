from django.contrib import admin
from .models import Employee, Department, Designation


class EmployeeInline(admin.StackedInline):
    model = Employee
    extra = 2


class DesignationAdmin(admin.ModelAdmin):

    inlines = [EmployeeInline]


class EmployeeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal info', {'fields': ['name']}),
        (None, {'fields': ['email']}),
        ('Profile info', {'fields': ['department']}),
        (None, {'fields': ['designation']}),
    ]

    """ departments in list_display is the method of Employee class,
        department in the list_filter is the field"""

    list_display = ('name', 'email', 'departments', 'designation')
    list_filter = ('designation', 'department', )


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department)
admin.site.register(Designation, DesignationAdmin)
