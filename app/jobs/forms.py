from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import Job
from app.accounts.models import Candidate, Company

# - Register/Create a user

class CreateCompanyUserForm(UserCreationForm):

    class Meta:

        model = Company
        fields = ['email', 'password1', 'password2']

class CreateCandidateUserForm(UserCreationForm):

    class Meta:

        model = Candidate
        fields = ['email', 'password1', 'password2', 'expected_salary', 'experience', 'last_education']



# - Login a user

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# - Create a record

class CreateJobForm(forms.ModelForm):

    class Meta:

        model = Job
        fields = ['name', 'salary_range', 'requirements', 'schooling']


# - Update a record

class UpdateJobForm(forms.ModelForm):

    class Meta:

        model = Job
        fields = ['name', 'salary_range', 'requirements', 'schooling']