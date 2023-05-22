from django.contrib import admin
from .models import *

# Register your models here.
class UserImageInLine(admin.TabularInline):
    model= UserImage
    max_num = 1

@admin.register(User)   #кастомизированная моделька, поэтому у нее такое усложненная регистрация
class PostAdmin(admin.ModelAdmin):
    inlines = [UserImageInLine,]