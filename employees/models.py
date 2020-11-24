from django.db import models
import datetime
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
    
    def __str__(self):
        return self.first_name + ' '+ self.last_name
    


class Supervisor(models.Model):
    Supervisor = models.ForeignKey(Employee, on_delete=models.CASCADE,null=True)
    soburdinate = models.ForeignKey(Employee,related_name="subordinates",null=True,on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=True,null=True)


class ExcelFiles(models.Model):
    file = models.FileField(upload_to='excel_files')
    created_at = models.DateTimeField( default=datetime.datetime.now())
