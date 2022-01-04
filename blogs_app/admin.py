from django.contrib import admin
from .models import Blog
# Register your models here.

admin.site.register(Blog)
admin.site.site_header = 'Astar Administration'
admin.site.site_title = 'Astar'