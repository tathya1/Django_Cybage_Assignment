from django.contrib import admin
from .models import Employee, Department, Designation


class EmployeeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal info', {'fields': ['name']}),
        (None, {'fields': ['email']}),
        ('Profile info', {'fields': ['department']}),
        (None, {'fields': ['designation']}),
    ]
    list_display = ('name', 'email','departments', 'designation')

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Department)
admin.site.register(Designation)
