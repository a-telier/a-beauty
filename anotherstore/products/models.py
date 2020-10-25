from django.db import models

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
    price = models.DecimalField(default="Price", decimal_places=2, max_digits=1000)
    itemNo = models.IntegerField(default="ItemNo")
    image = models.FileField()
    additionalImages = models.FileField()
