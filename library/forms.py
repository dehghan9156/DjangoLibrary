from django import forms
from .models import Amanat

class AmanatForm(forms.ModelForm):
    class Meta:
        model = Amanat
        fields = ["startdate","returndate"]
        widgets = {
            'startdate': forms.DateTimeInput(attrs={
                'class': 'form-control',
            }),
            'returndate': forms.DateTimeInput(attrs={
                'class': 'form-control',
            }),
        }