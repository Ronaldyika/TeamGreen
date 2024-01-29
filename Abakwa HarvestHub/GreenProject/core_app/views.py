from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from .models import Updates

# Home page
def homepage(request):
    return render(request,'index.html')
# Registration
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)    
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'Authentication/register.html', {'form': form})
    
# managing updates
def get_updates(request):
    updates = Updates.objects.all()
    return render(request, 'updates.html', {'updates': updates})