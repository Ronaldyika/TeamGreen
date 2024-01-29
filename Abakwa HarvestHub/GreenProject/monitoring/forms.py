from django import forms
from .models import Farm_info

class CreateFarmForm(forms.ModelForm):
    class Meta:
        model = Farm_info
        fields = ['name','moisture', 'temperature', 'light_intensity', 'humidity', 'soil_ph']