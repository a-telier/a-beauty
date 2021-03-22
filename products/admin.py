from django.contrib import admin
#   relative import (same directory), importing product class from models
from .models import Product, Category


class ProductAdmin (admin.ModelAdmin):
    list_display = (
        'category',
        'brand',
        'name',
        'sku',
        'price',
        'image',
    )

class CategoryAdmin (admin.ModelAdmin):
    list_display = (
        'name',
        'display_name',
        'teaser',
    )


#   Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)