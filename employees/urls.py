from django.urls import path
from .views import employeeListView,addEmployee,congratsPageView,supervisorsView,addSupervisorView,makeSupervisorView,assignSupervisor,assignCongratsPageView,uploadExcelPageView
urlpatterns = [
    path('',employeeListView),
    path('add',addEmployee),
    path('add-bulk',uploadExcelPageView),
    path('congrats',congratsPageView),
    path('supervisors',supervisorsView),
    path('supervisors/add',addSupervisorView),
    path('supervisors/add/<int:pk>',makeSupervisorView),
    path('assign-supervisor',assignSupervisor),
    path('assign-supervisor/congrats',assignCongratsPageView),
]
