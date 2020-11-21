from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    date_of_birth =models.DateField( auto_now=False, auto_now_add=False)
    date_of_employment = models.DateField(auto_now=False, auto_now_add=False)
    position =  models.CharField( max_length=50)
    position = models.FloatField()
    user_instance = models.ForeignKey("users.User", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_At = models.DateTimeField(auto_now=True, auto_now_add=False)


class Supervisor(models.Model):
    employee_iprofile = models.ForeignKey(Employee, on_delete=models.CASCADE)
    employee = models.ManyToManyField(Employee,related_name="subordinates")

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_At = models.DateTimeField(auto_now=True, auto_now_add=False)
