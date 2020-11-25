
from celery import shared_task
from .models import Employee,ExcelFiles
from utils.date_format import getAge

from users.models import User
import logging

@shared_task
def createEmployee(data):

    try:
        print(data)
        user = User.objects.create(password = data[3],email = data[2])
        employee_create = Employee.objects.create(first_name = data[0],last_name=data[1],date_of_birth = data[4],date_of_employment = data[5],user_instance = user,position = data[6],salary = data[7])
        employee = Employee.objects.filter(pk = employee_create.pk).first()
        employee.age = getAge(employee.date_of_birth)
        employee.save()
    except:
        logging.ERROR('Failed to create user because of integrity error')


