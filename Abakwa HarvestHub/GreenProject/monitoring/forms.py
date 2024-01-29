from django import forms
from .models import Farm_info

class CreateFarmForm(forms.ModelForm):
    class Meta:
        model = Farm_info
        fields = ['name']