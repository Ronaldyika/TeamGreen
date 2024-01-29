from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User


def homepage(request):
    return render(request,'index.html')

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)    
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'Authentication/register.html', {'form': form})
    
# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)

#             if user is not None:
#                 login(request, user)
#                 return redirect('homepage')
#             else:
#                 error_message = 'Invalid credentials. Please check your username and password.'
#                 return render(request, 'registration/login.html', {'error': error_message})
#     else:
#         form = LoginForm()

#     return render(request, 'Authentication/login.html', {'form': form})