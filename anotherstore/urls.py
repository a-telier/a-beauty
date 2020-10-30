"""anotherstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#   Here we import all the views you want to route via url
#   ex. from pages.views import homepage_view, contact_view, about_view, etc
from pages.views import homepage_view, product_view
from products.views import product_detail_view


#   Here we store the urls we want to display ex. home for homepage_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage_view, name="home"),
    path('home/', homepage_view, name="home"),
    path('product/', product_detail_view, name="product"),
]
