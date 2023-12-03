from django import forms
from .models import Product_sub_cat

class ProductSubCatForm(forms.ModelForm):
    class Meta:
        model = Product_sub_cat
        fields = ['product_price', 'product_image', 'product_model', 'product_ram']
