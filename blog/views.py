from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views import generic
from .models import Article, Blog_category

from products.models import Product, Category


# Create your views here.
def all_articles(request):
    articles = Article.objects.all()
    all_categories = Category.objects.all()
    # blog_categories = None

    # if 'blog_category' in request.GET:
    #     blog_categories = request.GET['blog_category'].split(',')
    #     articles = articles.filter(category__name__in=blog_categories)
    #     blog_categories = blog_category.objects.filter(name__in=blog_categories)

    context = {
        'articles': articles,
        'categories': all_categories,
        # 'blog_categories': blog_categories,
    }

    return render(request, "blog/all_articles.html", context)


def article_detail(request, article_url):
    article = get_object_or_404(Article, url=article_url)
    articles = Article.objects.all()
    all_categories = Category.objects.all()

    context = {
        'article': article,
        'articles': articles,
        'categories': all_categories,
    }

    return render(request, "blog/article.html", context)