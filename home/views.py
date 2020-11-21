from django.shortcuts import render

def homeScreenView(requst):
    # print(requst.user.is_authenticated)
    user = requst.user
    if  user.is_authenticated:
        return render(requst,'home.html',{'user':user})
    else:
        return render(requst,'landing.html')

    
