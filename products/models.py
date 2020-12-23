from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.
# CATEGORIES = {
#     ("Eyes", "Eyes"),
#     ("Lips", "Lips"),
#     ("Face", "Face")
# }

class Category(models.Model):
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.IntegerField(default=000000)
    brand = models.CharField(default='Brand Name', max_length=120)
    name = models.TextField(default='Product Name')
    description = models.TextField(default='Product Description', blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.FileField(default="", null=True, blank=True, upload_to='products')
    additionalImages = models.FileField(default="", null=True, blank=True, upload_to='additional')

    def __str__(self):
        return self.name