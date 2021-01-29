from django.shortcuts import render, get_object_or_404, redirect  #  renders HTML templates
from django.http import HttpResponse #  displays HttpResponse
from django.shortcuts import render

from products.models import Product, Category

# Here are the views that we created.
def index(request):
    return render(request, "home/index.html")

