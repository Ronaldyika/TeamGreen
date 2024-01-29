from django.shortcuts import render, redirect
from .models import Farm_info
from django.contrib.auth.decorators import login_required
from .forms import CreateFarmForm

# Create your views here.

#creating a farm
@login_required
def getFarmInfo(request):
    farm_info = Farm_info.objects.first()
    return render(request, 'farm.html', {'farm_info': farm_info})

# Creating a farm

def createFarm(request):
    form = CreateFarmForm()
    if request.method == "POST":
        form = CreateFarmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('getFarmInfo')
    else:
        return render(request, 'createfarm.html', {'form': form})