from django.shortcuts import render

# Create your views here.

def categories(request):
  return render(request, 'categories_app/categories.html')