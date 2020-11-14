from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    query = None
    sort = None

    return render(request, "products/detail.html")

def product_detail(request):
    return render(request, "products/detail.html")