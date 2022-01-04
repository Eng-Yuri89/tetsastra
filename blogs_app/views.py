from django.shortcuts import render
from .models import Blog
# Create your views here.

def blog(request):
  return render(request, 'blogs_app/blogs.html', {'blog': Blog.objects.all()})