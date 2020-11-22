from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    date_of_birth =models.DateField( auto_now=False, auto_now_add=False)
    date_of_employment = models.DateField(auto_now=False, auto_now_add=False)
    position =  models.CharField( max_length=50)
    salary = models.IntegerField(default=0)
    user_instance = models.ForeignKey("users.User", on_delete=models.CASCADE)
    is_supervisor = models.BooleanField(default = False)
    
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=True,null=True)


class Supervisor(models.Model):
    employee_profile = models.ForeignKey(Employee, on_delete=models.CASCADE,null=True)
    soburdinate = models.ManyToManyField(Employee,related_name="subordinates",null=True)

    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=True,null=True)


# class excelFiles(models.Model):
#     file = models.FileField(upload_to='/')