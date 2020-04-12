from django import forms
from django.contrib.auth.models import User
from login_out.models import UserProfileInfo

class User_Form(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username' , 'email', 'password')

class User_Profile_Form(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('name' , 'DOB')


class login_form(forms.Form):
    USERNAME = forms.CharField()
    PASSWORD = forms.CharField(widget = forms.PasswordInput())
