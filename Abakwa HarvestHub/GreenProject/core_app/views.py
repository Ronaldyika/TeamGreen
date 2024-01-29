from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User


def homepage(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            location = form.cleaned_data.get('location')
            phone = form.cleaned_data.get('phone')
            password = form.cleaned_data.get('password')
            password2 = form.cleaned_data.get('password2')
            
            user = User.objects.create_user(username=username, email=email, password=password)
            
            # Add custom fields to the user instance
            user.location = location
            user.phone = phone
            user.save()
            
            # Authenticate and login the user
            user = authenticate(request, username=username, password=password)
            login(request, user)
            
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'Authentication/register.html', {'form': form})
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            error_message = 'Invalid credentials. Please check your username and password.'
            return render(request, 'registration/login.html', {'error': error_message})
    else:
        return render(request, 'Authentication/login.html')
