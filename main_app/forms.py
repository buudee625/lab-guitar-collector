from django.forms import ModelForm
from .models import Review
from django import forms

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__' #['rating', 'review']

        widgets = {
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'review': forms.Textarea(attrs={'class': 'form-control'}),
        }