from django.shortcuts import render

# Create your views here.

def logPageView(request):
    return render(request,'logs.html')