from django import forms
from .models import Amanat

class AmanatForm(forms.ModelForm):
    class Meta:
        model = Amanat
        fields = ["startdate","returndate"]
        widgets = {
            'startdate': forms.DateTimeInput(attrs={
                'type':'date',
                'class': 'form-control',
            }),
            'returndate': forms.DateTimeInput(attrs={
                'type':'date',
                'class': 'form-control',
            }),
        }
    def clean(self):
        cleaned_data = super().clean()
        startdate = cleaned_data.get("startdate")
        returndate = cleaned_data.get("returndate")
        if startdate and returndate:
            if returndate <= startdate:
                raise forms.ValidationError("The return date must be after the start date.")
        return cleaned_data
