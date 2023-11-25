# forms.py
from django import forms
from .models import Fertilisation

class FertilisationForm(forms.ModelForm):
    class Meta:
        model = Fertilisation
        fields = '__all__'
