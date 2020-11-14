from django.shortcuts import render, get_object_or_404, redirect  #  renders HTML templates
from django.http import HttpResponse #  displays HttpResponse
from products.models import Product

# obj = Product.objects.get(id=1)

#     'additionalImages': obj.additionalImages

# Here are the views that we created.
def index(request):
    # obj = get_object_or_404(Product, id=2)
    # context = {
    #     'category': obj.category,
    #     'brand': obj.brand,
    #     'product': obj.product,
    #     'variant': obj.variant,
    #     'productDescription': obj.productDescription,
    #     'price': obj.price,
    #     'itemNo': obj.itemNo,
    #     'image': obj.image,
    #     'additionalImages': obj.additionalImages
    #     }
    return render(request, "home.html")

def product_view(request):
    return render(request, "product/detail.html")
