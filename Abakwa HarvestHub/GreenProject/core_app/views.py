from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm

def homepage(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('homepage')
        else:
            form = RegisterForm()
        return render(request, 'registration/register.html', {'form': form})
    
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return render(request, 'registration/login.html',{'error': 'Invalid Credentials'} )
    else:
        return render(request, 'registration/login.html')