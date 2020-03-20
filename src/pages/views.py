from django.http import HttpResponse
from django.shortcuts import render

def homepage_view(request, *args, **kwarg): # *args, **kwargs
    print(request.user)
    #return HttpResponse("<h1>Hello World</h1>")  # string of HTML code
    return render(request, "home.html",  {} ) 

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {} ) 

def about_view(request, *args, **kwargs):
    my_context = {
            "my_text": "This is about me" ,
            "my_number": 123 ,
            "this_is_true": True ,
            "my_list": [123, 321, 213, 'Hello'],
            "my_html": "<h1>Hello World</h1>"
    }
    return render(request, "about.html",  my_context ) 
