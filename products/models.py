from django.contrib.postgres.fields import ArrayField
from django.db import models
from django import forms

from django.contrib import admin


###     CATEGORIES    ###
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)
    banner = models.FileField(default="", null=True, blank=True, upload_to='categories/banner')
    teaser = models.FileField(default="", null=True, blank=True, upload_to='categories/teaser')

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


###     PRODUCTS    ###
# List of ratings that will be used for Products model
RATINGS = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
]

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=100, default=000000)
    brand = models.CharField(default='Brand Name', max_length=120)
    name = models.TextField(default='Product Name')
    description = models.TextField(default='Product Description', blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.IntegerField(choices=RATINGS, blank=True, null=True)
    image = models.FileField(default="", null=True, blank=True, upload_to='products')
    additionalImages = models.FileField(default="", null=True, blank=True, upload_to='additional')
    new = models.BooleanField(default="False", null=True)
    deals = models.BooleanField(default="False", null=True)

    def __str__(self):
        return self.name


#   Save As instead of Save and continue
#   credits: https://www.nuomiphp.com/eplan/en/471509.html
#   class PersonAdmin(admin.ModelAdmin):
#   save_as = True