from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'  
        ]

class RawProductForm(forms.Form):
    title = forms.CharField(
        label='Title from field',
        widget=forms.TextInput(
        attrs={
            "placeholder": "type a title"
        }
        )
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
        attrs={
            "placeholder": "type a description",
            "class": "new-class-name",
            "rows": 1 ,
            'cols': 20
        }
        )
)
    price       = forms.DecimalField(initial=199.99)   