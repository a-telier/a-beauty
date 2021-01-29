from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views import generic
from .models import Article

# Create your views here.
def all_articles(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, "blog/all_articles.html", context)


def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    articles = Article.objects.all()

    context = {
        'article': article,
        'articles': articles,
    }

    return render(request, "blog/article.html", context)