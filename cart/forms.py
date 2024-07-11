from django import forms
from product.models import Product
from django.utils.translation import gettext_lazy as _



class CartAddForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1, label="Quantity")
    override = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)
    