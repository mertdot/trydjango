from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title   = forms.CharField(label='Title',
                widget=forms.TextInput(attrs={"placeholder": "Your Title"}))
    email   = forms.EmailField()
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
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'  
        ]
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "CFE" in title:
            return title
        else:
            raise forms.ValidationError("This is not a valid title")

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("title")
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not edu mail!")
            return email





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