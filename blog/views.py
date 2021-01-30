from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views import generic
from .models import Article, Blog_category

from products.models import Product, Category


# Create your views here.
def all_articles(request):
    articles = Article.objects.all()
    all_categories = Category.objects.all()
    blog_categories= Blog_category.objects.all()

    context = {
        'articles': articles,
        'all_categories': all_categories,
        'blog_categories': blog_categories,
    }

    return render(request, "blog/all_articles.html", context)


def article_detail(request, article_url):
    article = get_object_or_404(Article, url=article_url)
    articles = Article.objects.all()
    all_categories = Category.objects.all()
    blog_categories= Blog_category.objects.all()

    context = {
        'article': article,
        'articles': articles,
        'all_categories': all_categories,
        'blog_categories': blog_categories,
    }

    return render(request, "blog/article.html", context)