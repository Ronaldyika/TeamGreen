from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Updates,TutorialPoint,CreditUnion

# Home page
def homepage(request):
    return render(request,'index.html')

@login_required
def indexpage(request):
    return render(request,'dashboard/main.html')
# Registration
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)    
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'Authentication/register.html', {'form': form})

@login_required
def credit_union(request):
    details = CreditUnion.objects.all()
    return render(request,'dashboard/credit_union.html',{'details':details})

@login_required
def profile(request):
    return render(request,'farmersguide/profile.html')
# managing updates
@login_required
def get_updates(request):
    details = TutorialPoint.objects.all()
    query_set = Updates.objects.all()
    return render(request, 'Authentication/notification/notification.html', {'query_set': query_set,'details':details})
	