from django import forms
from django.forms import TextInput

from .models import Products



class AddProductForm(forms.ModelForm):
    class Meta:
        model = Products
        exclude = ['owner'] #the form will take all the fields except owner
        labels = {'name': 'product Name'} #adding labels
        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Enter the name of the product',
            })
        }
