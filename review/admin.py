from django.contrib import admin

# Register your models here.
from .models import Rating, Favorite

# Register your models here.

# admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Favorite)