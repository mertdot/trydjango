from django.shortcuts import render
 
from .models import Product
from .forms import ProductForm, RawProductForm


""" def product_create_view(request):
        my_form = RawProductForm()
        if request.method == "POST":
            my_form = RawProductForm(request.POST)
            if my_form.is_valid():
                #Django sure to data is trusted
                Product.objects.create(**my_form.cleaned_data)
            else:
                print(my_form.errors)
        context = {
            "form": my_form
        }
        return render(request, "products/product_create.html", context)
 """
 
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form' : form
    }

    return render(request, "products/product_create.html", context)






def product_detail_view(request):
    obj = Product.objects.get(id=1)

    #context = {
    #    'title': obj.title,
    #    'description': obj.description
    #}

    context = {
        'object' : obj
    }

    return render(request, "products/product_detail.html", context)

    def render_initial_data(request):
        initial_data = {
            'title': "My awesome title"
            }
        form = RawProductForm(request.POST or None, initial=initial_data)
        context = {
            'form' : form
        }

        return render(request, "products/product_create.html", context)
