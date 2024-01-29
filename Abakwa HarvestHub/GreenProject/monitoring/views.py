from django.shortcuts import render, redirect
from .models import Farm_info
from django.contrib.auth.decorators import login_required
from .forms import CreateFarmForm

# Create your views here.


@login_required
def createFarm(request):
    form = CreateFarmForm()
    if request.method == 'POST':
        form = CreateFarmForm(request.POST)
        if form.is_valid():
            farm_info = form.save(commit=False)
            farm_info.user_id = request.user
            farm_info.save()
            return redirect('get_farm_info')
    else:
        return render(request, 'createfarm.html', {'form': form})
    
