from django.db import models

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
    email = models.EmailField(unique=True, blank=False)
    department = models.ManyToManyField(Department)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)

    def __str__(self):
        return self.name