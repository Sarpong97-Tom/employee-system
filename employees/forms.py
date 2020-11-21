from django import forms
from .models import Employee,Supervisor


class EmployeeForms(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"