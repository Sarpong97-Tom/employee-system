from django.shortcuts import render
from utils.log_utils import getLoagList
# Create your views here.

def logPageView(request):
    logs = getLoagList()
    return render(request,'logs.html',{'logs':logs})