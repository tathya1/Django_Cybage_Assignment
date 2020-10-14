from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Department(models.Model):
    departmentName = models.CharField(max_length=100)

    def __str__(self):
        return self.departmentName


class Designation(models.Model):
    designationName = models.CharField(max_length=100)

    def __str__(self):
        return self.designationName


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False)
    department = models.ManyToManyField(Department, blank=True)
    designation = models.ForeignKey(
        Designation, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    """to use in admin.py for  displaying the departments, 
    as it is M2M making a method here or at EmployeeAdmin class will do the job"""

    def departments(self):

        return ",".join([d.departmentName for d in self.department.all()])
