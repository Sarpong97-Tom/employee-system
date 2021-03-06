from django import forms
from .models import Employee,Supervisor,ExcelFiles
from users.models import User
from utils.get_file_extention import getFileExtention
from utils.date_format import getTodaysDate
from utils.excel_utils import loadWorksheet

class EmployeeForms(forms.Form):
    first_name = forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Enter first name"}))
    last_name = forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Enter last name"}))
    email = forms.EmailField(max_length=100,required=True,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':"Enter email"}))
    password = forms.CharField(max_length=100,required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':"Enter password"}))
    password_confirm = forms.CharField(max_length=100,required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':"Confirm password"}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','placeholder':"YYYY-MM-DD"}))
    date_of_employment = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','placeholder':"YYYY-MM-DD"}))
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
        dob = self.cleaned_data.get('date_of_birth')

        if getTodaysDate()<=dob:
            self.errors['date_of_birth'] = self.error_class(['Date picked is more than today'])
        return self.cleaned_data



class SuperVisorForm(forms.ModelForm):
    supervisor = forms.ModelChoiceField(Employee.objects.filter(is_supervisor = True),required=True,widget=forms.Select(attrs={'class':'form-control'}))
    soburdinate = forms.ModelChoiceField(Employee.objects.all(),required=True,widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = Supervisor
        fields = ['supervisor','soburdinate']

    def clean(self,*args, **kwargs):
         #Prevent assigning employee to supervisor several times
        supervisor = self.cleaned_data.get('supervisor')
        soburdinate = self.cleaned_data.get('soburdinate')
        
        try:
            supervising = Supervisor.objects.get(Supervisor = supervisor.id)
            if supervising.soburdinate == soburdinate:
                self.errors['supervisor'] = self.error_class(['Supervisor already assigned to user'])
        except Supervisor.DoesNotExist:
            pass
        if supervisor.id == soburdinate.id:
            self.errors['supervisor'] = self.error_class(['You cannot add supervisor to self'])
        return self.cleaned_data

class ExcelUploadForm(forms.ModelForm):
    file = forms.FileField(allow_empty_file=False,required=True,help_text='upload excel file containing employees data',widget=forms.FileInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = ExcelFiles
        fields = ['file']

    def clean(self,*args, **kwargs):
        file = self.cleaned_data.get('file')

        if(file == None):
            self.errors['file'] = self.error_class(['File cannot be empty'])
        
        ext = getFileExtention(file)
        if ext != 'xlsx':
            self.errors['file'] = self.error_class(['File must be an excel file'])
        # num_culumn = len(list(loadWorksheet(file).rows))
        # if len(list(loadWorksheet(file).rows)) != 8:
        #     self.errors['file'] = self.error_class(['File has a missing culumn'])
        return  self.cleaned_data

