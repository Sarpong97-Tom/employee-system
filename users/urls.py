from django.urls import path
from .views import loginView,congratsPageView,logoutView

urlpatterns = [

     path('login',loginView),
     path('congrats',congratsPageView),
     path('logout',logoutView)
    #  path('me',AuthUserView.as_view()),
    #  path('register_admin',RegisterAdmin.as_view()),
 ]
 