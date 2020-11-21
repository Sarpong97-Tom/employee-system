from django.shortcuts import render

def homeScreenView(requst):
    print(requst)
    return render(requst,'base.html',{})
