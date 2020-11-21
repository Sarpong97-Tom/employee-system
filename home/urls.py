from django.urls import path
from .views import homeScreenView
urlpatterns = [
    path('',homeScreenView)
]
