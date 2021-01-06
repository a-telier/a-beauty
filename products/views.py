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


#   This view allows you to view each product individually
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, "products/product_detail.html", context)