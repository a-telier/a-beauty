from django.contrib import admin

# relative import (same directory), importing product class from models
from .models import Product

# Register your models here.
admin.site.register(Product)