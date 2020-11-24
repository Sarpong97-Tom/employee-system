from django.shortcuts import render
import logging

def homeScreenView(requst):
    # print(requst.user.is_authenticated)
    logging.error('Stiilll')
    logging.info('Try info')
    user = requst.user
    if  user.is_authenticated:
        return render(requst,'home.html',{'user':user})
    else:
        return render(requst,'landing.html')

    
