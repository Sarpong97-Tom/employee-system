from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100,required=True,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':"Enter email"}))
    password = forms.CharField(max_length=100,required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':"Enter password"}))