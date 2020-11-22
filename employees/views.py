from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForms
from users.models import User
# Create your views here.
def employeeListView(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('/auth/login')
    else:
        employees = Employee.objects.all()
        return render(request,'employees.html',{'employees':employees})

def addEmployee(request):
    form = EmployeeForms()
    user = request.user
    if not user.is_authenticated:
        return redirect('/auth/login')
    else:
        if request.method == 'GET':
            return render(request,'add_employee.html',{'form':form})
        else:
            form = EmployeeForms(data=request.POST)
            if form.is_valid():
                user = User.objects.create_user(request.POST['email'],password=request.POST['password'])
                employee = Employee.objects.create(first_name = request.POST['first_name'],last_name = request.POST['first_name'],age =request.POST['age'],date_of_birth = request.POST['date_of_birth'],
                date_of_employment = request.POST['date_of_employment'],position = request.POST['position'],salary = request.POST['salary'],user_instance = request.user
                 )
                return redirect('/employees/congrats')
            else:
                return render(request,'add_employee.html',{'form':form})
            
def congratsPageView(request):
    return render(request,'employee_congrats.html')