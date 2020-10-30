from django.shortcuts import render
from .models import Product

# Create your views here.
def product_detail_view(request):
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
    return render(request, "product/detail.html", product)