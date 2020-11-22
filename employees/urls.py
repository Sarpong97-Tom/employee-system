from django.urls import path
from .views import employeeListView,addEmployee,congratsPageView,supervisorsView,addSupervisorView,makeSupervisorView
urlpatterns = [
    path('',employeeListView),
    path('add',addEmployee),
    path('congrats',congratsPageView),
    path('supervisors',supervisorsView),
    path('supervisors/add',addSupervisorView),
    path('supervisors/add/<int:pk>',makeSupervisorView),
]
