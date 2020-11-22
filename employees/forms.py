from django import forms
from .models import Employee,Supervisor
from users.models import User


class EmployeeForms(forms.Form):
    first_name = forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Enter first name"}))
    last_name = forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Enter last name"}))
    email = forms.EmailField(max_length=100,required=True,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':"Enter email"}))
    password = forms.CharField(max_length=100,required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':"Enter password"}))
    password_confirm = forms.CharField(max_length=100,required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':"Confirm password"}))
    age = forms.IntegerField(max_value=300,widget=forms.NumberInput(attrs={'class':'form-control','placeholder':"Enter age"}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','placeholder':"Enter date of birth"}))
    date_of_employment = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','placeholder':"Enter date of employment"}))
    position = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Enter position"}))
    salary = forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':"Enter salary"}))

    def clean(self,*args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        users = User.objects.filter(email = email)

        if(len(users)>0):
            self.errors['email'] = self.error_class(['Email has already been taken'])
        if (password != password_confirm):
            self.errors['password'] = self.error_class(['Passwords do not match'])
            self.errors['password_confirm'] = self.error_class(['Passwords do not match'])


class SuperVisorForm(forms.ModelForm):
    class Meta:
        model = Supervisor
        fields = ['employee_profile','soburdinate']
