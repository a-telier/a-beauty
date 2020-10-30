from django.shortcuts import render  #  renders HTML templates
from django.http import HttpResponse #  displays HttpResponse
from products.models import Product

obj = Product.objects.get(id=1)

product = {
    'category': obj.category,
    'brand': obj.brand,
    'line': obj.line,
    'lineDescription': obj.lineDescription,
    'product': obj.product,
    'variant': obj.variant,
    'productDescription': obj.productDescription,
    'ingredients': obj.ingredients,
    'price': obj.price,
    'itemNo': obj.itemNo,
    'image': obj.image,
    'additionalImages': obj.additionalImages
}


# Here are the views that we created.
def homepage_view(request, *args, **kwargs):
    #   *args (Non Keyword Arguments)
    #   **kwargs (Keyword Arguments)
    #   Used as an argument when we are unsure about the number of arguments
    #   to pass in the functions
    #   print(args, kwargs)
    #   prints the user that has requested the page
    #   print(request.user)
    #   return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", product)

def product_view(request, *args, **kwargs):
    return render(request, "product/detail.html")
