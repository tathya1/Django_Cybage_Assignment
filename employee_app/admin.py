from django.contrib import admin
from .models import Employee, Department, Designation

# Register your models her
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Designation)