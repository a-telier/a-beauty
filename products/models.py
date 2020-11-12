from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.
CATEGORIES = {
    ("Eyes", "Eyes"),
    ("Lips", "Lips"),
    ("Face", "Face")
}

class Product(models.Model):
    category = models.CharField(choices=CATEGORIES, max_length=10)
    brand = models.CharField(default="Brand Name", max_length=120)
    product = models.TextField(default="Product Name")
    variant = models.TextField(default="Variant Name")
    productDescription = models.TextField(default="Product Description", blank=True, null=True)
    price = models.DecimalField(default="Price", decimal_places=2, max_digits=1000)
    itemNo = models.IntegerField(default="ItemNo")
    image = models.FileField(upload_to="products")
    additionalImages = models.FileField(blank=True, upload_to="additional")