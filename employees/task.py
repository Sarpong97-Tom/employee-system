
from celery import shared_task
from .models import Employee,ExcelFiles

from users.models import User
import logging

@shared_task
def createEmployee(data):
    print(data)
    user = User.objects.create(password = data[3],email = data[2])
    Employee.objects.create(first_name = data[0],last_name=data[1],date_of_birth = data[4],date_of_employment = data[5],user_instance = user,position = data[6],salary = data[7])

