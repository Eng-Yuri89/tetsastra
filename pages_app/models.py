from django.db import models

# Create your models here.

class Boxes(models.Model):
    image = models.ImageField(upload_to='images/%y/%m/%d')
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title

class Catig(models.Model):
    title = models.CharField(max_length=60)
    def __str__(self):
        return self.title

class Home(models.Model):
    image = models.ImageField(upload_to='images/%y/%m/%d')
    nums = models.IntegerField(default=1)
    new_coll = models.CharField(max_length=80)
    def __str__(self):
        return self.new_coll

class Products(models.Model):
    image = models.ImageField(upload_to='images/%y/%m/%d')
    tag = models.CharField(max_length=30, null=True, blank=True)
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    rrp = models.CharField(max_length=30, null=True, blank=True)
    add = models.CharField(max_length=40, default='add to cart')
    def __str__(self):
        return self.title