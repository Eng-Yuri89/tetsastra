from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to= 'images/%y/%m/%d')
    active = models.BooleanField(default=True)