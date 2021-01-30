from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views import generic

from .models import Article, Blog_category
from products.models import Category


# Create your views here.
def all_articles(request):
    articles = Article.objects.all()
    all_blog_categories = Blog_category.objects.all()
    all_categories = Category.objects.all()
    blog_categories = None

    print('all_categories')
    print(all_blog_categories)

    #   Category filtering
    if 'blog_category' in request.GET:
        blog_categories = request.GET['blog_category'].split(',')
        articles = articles.filter(blog_category__name__in=blog_categories)
        blog_categories = Blog_category.objects.filter(name__in=blog_categories)

    context = {
        'articles': articles,
        'all_categories': all_categories,
        'all_blog_categories': all_blog_categories,
        'blog_categories': blog_categories,
    }

    return render(request, "blog/all_articles.html", context)


def article_detail(request, article_url):
    article = get_object_or_404(Article, url=article_url)
    articles = Article.objects.all()
    all_blog_categories = Blog_category.objects.all()
    all_categories = Category.objects.all()

    context = {
        'article': article,
        'all_categories': all_categories,
        'articles': articles,
        'all_blog_categories': all_blog_categories,
    }

    return render(request, "blog/article.html", context)