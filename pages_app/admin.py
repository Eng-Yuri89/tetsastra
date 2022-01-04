from django.contrib import admin
from .models import Boxes, Catig, Home, Products

# Register your models here.
admin.site.register([Boxes, Catig, Home, Products])