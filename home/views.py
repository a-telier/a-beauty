from django.shortcuts import render, get_object_or_404, redirect  #  renders HTML templates
from django.http import HttpResponse #  displays HttpResponse
from django.shortcuts import render

from products.models import Product, Category
from blog.models import Article, Blog_category

# Here are the views that we created.
def index(request):
    products = Product.objects.all()
    articles = Article.objects.all()
    all_categories = Category.objects.all()

    context = {
        'products': products,
        'articles': articles,
        'all_categories': all_categories,
    }

    return render(request, "home/index.html", context)

