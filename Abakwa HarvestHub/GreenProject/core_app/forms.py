from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=False)
    location = forms.CharField(max_length=50,required=False)
    phone_number = forms.IntegerField(required=True)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(max_length=50, required=True)