from django.shortcuts import render

from .models import Boxes, Catig, Home, Products


# Create your views here.

def index(request):
    box = Boxes.objects.all()
    home = Home.objects.all()
    cating = Catig.objects.all(),
    product = Products.objects.all()
    context = {'box': box, 'home': home, 'catig': cating,
               'product': product}
    return render(request, 'pages_app/index.html', context
                  )
