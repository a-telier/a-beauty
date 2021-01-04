from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category

# Create your views here.

#   This view allows you to see all products
def all_products(request):
    products = Product.objects.all()
    categories = Category.objects.all()[0:4]
    query = None
    sort = None

    context = {
        'products': products,
        'categories': categories,
    }

    return render(request, "products/products.html", context)