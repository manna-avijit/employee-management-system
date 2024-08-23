from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=50, null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} {self.location}'
    


class Role(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name
    


class Employee(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phone = models.IntegerField()
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    hireDate = models.DateField()
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s" %(self.firstName, self.lastName, self.phone)
    