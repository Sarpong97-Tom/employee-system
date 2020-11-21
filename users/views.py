from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm


def loginView(request):
    form = LoginForm()
    if request.method == "GET":
        user = request.user
        if user.is_authenticated:
            return redirect('/')
        return render(request,'login.html',{'form':form})
    elif request.method == 'POST':
        print(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(email=email, password=password)
            print(user)
            if user is not None:
                login(request,user)
                return redirect('/auth/congrats')
            else:
                return render(request,'login.html',{'form':form,'message':'Invalid credntials'})
        else:
            return redirect('/auth/login')

def congratsPageView(request):
    return render(request,'congrats.html')

def logoutView(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('/auth/login')
    else:
        logout(request)
        return redirect('/auth/login')