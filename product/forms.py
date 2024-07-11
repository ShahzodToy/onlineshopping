from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields= ['name','review','emial']

class SearchForm(forms.Form):
    query = forms.CharField()