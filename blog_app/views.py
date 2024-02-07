from django.shortcuts import render, HttpResponse
from .models import Article, Category
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    return render(request, 'blog_app/login.html')


def registration_view(request):
    return render(request, 'blog_app/registration.html')


def home_view(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'blog_app/index.html', context)


def get_category_articles_views(request, category_id):
    category = Category.objects.get(pk=category_id)
    articles = Article.objects.filter(category=category)
    context = {
        'articles': articles
    }
    return render(request, 'blog_app/index.html', context)


def test_page(request):
    return render(request, 'blog_app/text_site.html')


def test_detail(request):
    return render(request, 'blog_app/text_detail.html')
