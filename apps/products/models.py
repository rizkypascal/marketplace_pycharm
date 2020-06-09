from django.db import models

# Create your models here.
class Product(models.Model):
    link = models.URLField()
    price = models.TextField()
    description = models.TextField()
    image_urls = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

class ProductPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.TextField()
    created_at = models.DateTimeField(auto_now=True)