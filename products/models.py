from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.core.files.storage import FileSystemStorage # customized file storage folder

# Customized location for product pictures storage
fsProducts = FileSystemStorage(location='/static/media/products'),
fsAdditional = FileSystemStorage(location='/static/media/additional')


# Create your models here.
CATEGORIES =( 
    ("Eyes", "Eyes"),
    ("Lips", "Lips"),
    ("Face", "Face")
)

class Product(models.Model):
    category = models.CharField(choices=CATEGORIES, max_length=10)
    brand = models.CharField(default="Brand Name", max_length=120)
    line = models.CharField(default="Line Name", max_length=120)
    lineDescription = models.TextField(default="Line Description", blank=True, null=True)
    product = models.TextField(default="Product Name")
    variant = models.TextField(default="Variant Name")
    productDescription = models.TextField(default="Product Description", blank=True, null=True)
    ingredients = ArrayField(models.CharField(max_length=200), blank=True)
    price = models.DecimalField(default="Price", decimal_places=2, max_digits=1000)
    itemNo = models.IntegerField(default="ItemNo")
    image = models.ImageField(storage=fsProducts)
    additionalImages = models.ImageField(blank=True, storage=fsAdditional)