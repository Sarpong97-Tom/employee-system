
from celery import shared_task
from .models import Employee,ExcelFiles
import logging

@shared_task
def createEmployee(data):
    user = User.objects.create(password = data[5],email = data[4])
    Employee.objects.create(first_name = data[0],last_name=data[1],age = data[2],date_of_birth = data[3],date_of_employment = data[3],user_instance = user)
    logging.info('{}{}'.format())

