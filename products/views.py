from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

# Create your views here.
def product_detail_view(request):

    obj = get_object_or_404(id=id)
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
    context = {
        'objects': obj
    }
    return render(request, "products/detail.html", context)