from django import forms
from django.forms import TextInput

from .models import Plants



class AddPlantForm(forms.ModelForm):
    class Meta:
        model = Plants
        exclude = ['owner'] #the form will take all the fields except owner
        labels = {'name': 'plant Name'} #adding labels
        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Enter the name of the plant',
            })
        }
