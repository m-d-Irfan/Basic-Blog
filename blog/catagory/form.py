from django import forms
from .models import Catagory

class cata_form(forms.ModelForm):
    class Meta:
        model = Catagory
        fields = ['name','parent']