from django.http import request
from django.shortcuts import render
# Create your views here.

# def product(request):
#   return render(request, 'products_app/product.html')

def products(request):
  return render(request, 'products_app/products.html')