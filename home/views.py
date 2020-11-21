from django.shortcuts import render

def homeScreenView(requst):
    # print(requst.user.is_authenticated)
    user = requst.user
    if  user.is_authenticated:
        return render(requst,'home.html')
    else:
        return render(requst,'landing.html',{})

    
