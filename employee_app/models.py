from django.db import models


class Organization(models.Model):
    organizationName = models.CharField(
        max_length=100, null=False, blank=False)

    def __str__(self):
        return self.organizationName

# def default_org():
#     return Organization.objects.get_or_create(organizationName="DefaultOrg")[0].id


class Department(models.Model):
    organization = models.ForeignKey(
        Organization, null=False, on_delete=models.CASCADE, related_name="dept")
    departmentName = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.departmentName}_{self.organization.organizationName}"


class Designation(models.Model):
    designationName = models.CharField(max_length=100)

    def __str__(self):
        return self.designationName


class UserProfile(models.Model):
    bio = models.CharField(max_length=100)

    def __str__(self):
        return self.bio


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False)
    bio = models.OneToOneField(
        UserProfile, null=True, on_delete=models.SET_NULL)
    department = models.ManyToManyField(
        Department, blank=False, related_name="emp")
    designation = models.ForeignKey(
        Designation, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    """to use in admin.py for  displaying the departments, 
    as it is M2M making a method here or at EmployeeAdmin class will do the job"""

    @property
    def departments(self):

        return ",".join([d.departmentName for d in self.department.all()])

    @property
    def organization(self):

        return ",".join(set([d.organization.organizationName for d in self.department.all()]))
