from django.urls import path
from .views import employeeListView,addEmployee,congratsPageView
urlpatterns = [
    path('',employeeListView),
    path('add',addEmployee),
    path('congrats',congratsPageView),
]
