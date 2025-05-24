from django import forms
from .models import Amanat,Book,Category

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

class BookForm(forms.ModelForm):
   class Meta :
        model = Book
        fields = ["category","name","image","description","year","pages"]
        widgets = {
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'image': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://example.com/image.jpg'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'year': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'pages': forms.TextInput(attrs={
                'class': 'form-control',
            }),
        }