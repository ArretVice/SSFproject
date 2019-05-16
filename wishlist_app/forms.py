from django import forms

from .models import WishlistItem


class AddItemForm(forms.ModelForm):
    class Meta:
        model = WishlistItem
        fields = ['item_name', 'price', 'url', 'comment']