from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    location = forms.CharField(max_length=100, help_text='Enter your location.')
    phone = forms.CharField(max_length=15, help_text='Enter your phone number.')

    class Meta:
        model = User
        fields = ['username', 'email', 'location', 'phone', 'password1', 'password2']



class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(max_length=50, required=True)