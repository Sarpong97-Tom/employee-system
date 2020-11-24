from django.urls import path
from .views import logPageView
urlpatterns = [
    path('',logPageView),
  
]
