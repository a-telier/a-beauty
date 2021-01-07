from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from .models import Product, Category

# Create your views here.

#   This view allows you to see all products
def all_products(request):
    products = Product.objects.all()
    query = None
 
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'No search criteria')
                return redirect(reverse('products'))

        # creating a Q object to pass a query
        # the pipe | generates the 'or' statement
        # i in front of contains make it not case sensitive
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, "products/products.html", context)


#   This view allows you to view each product individually
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    categories = Category.objects.all()

    context = {
        'product': product,
        'categories': categories,
    }

    return render(request, "products/product_detail.html", context)