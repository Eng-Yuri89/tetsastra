from django.db import models
from datetime import datetime

# Create your models here.

class Blog(models.Model):

    groups = [('Fasion','Fasion'), ('Models','Models'), ('Classes','Classes')]

    image = models.ImageField(upload_to='images/%y/%m/%d')
    date = models.DateTimeField(default=datetime.now)
    title = models.CharField(max_length=500, default='Type anythink')
    auther = models.CharField(max_length=50, default='Admin')
    group = models.CharField(max_length=50, default='Public', choices=groups)
    comment = models.IntegerField(default=1)
    content = models.TextField(default='Admin')

    def __str__(self):
        return self.title