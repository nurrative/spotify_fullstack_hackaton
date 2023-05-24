from django.contrib import admin
from .models import *


# Register your models here.
class SongFileInLine(admin.TabularInline):
    model= SongFile
    max_num = 1

@admin.register(Track)   #кастомизированная моделька, поэтому у нее такое усложненная регистрация
class TrackAdmin(admin.ModelAdmin):
    inlines = [SongFileInLine,]

admin.site.register(Artist) # это обычная регистрация какой то модели в админке