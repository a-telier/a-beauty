from django.contrib import admin
#   relative import (same directory), importing product class from models
from .models import Product, Category


class ProductAdmin (admin.ModelAdmin):
    list_display = (
        'sku',
        'brand',
        'name',
        'price',
        'image',
    )

class CategoryAdmin (admin.ModelAdmin):
    list_display = (
        'name',
        'display_name',
        'teaser',
        'banner',
    )


#   Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)