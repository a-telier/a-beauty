from django.contrib import admin

# relative import (same directory), importing product class from models
from .models import Product, Category

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)