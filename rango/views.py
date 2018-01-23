from django.shortcuts import render
#Importing the Category model
from rango.models import Category
from rango.models import Page

from django.http import HttpResponse

def index(request):

    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only- or all if less than 5
    # Place the list in our context_dict dictionary
    # that will be passed to the template engine.

    category_list= Category.objects.order_by('-likes')[:5]
    context_dict= {'categories': category_list}
               
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html')

def show_category(request, category_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict= {}

    try:
        # Can we find a category name slug with a given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category= Category.objects.get(slug=category_name_slug)

        # Retrieve all of the associated pages.
        # Note that filter() will return a list of page objects or an empty list
        pages= Page.objects.filter(category=category)

        #Adds our results list to the template context under name pages
        context_dict['pages']= pages

        context_dict['category']= category
    except Category.DoesNotExist:

        context_dict['category']= None
        context_dict['pages']= None

    return render(request, 'rango/category.html', context_dict)
