from django.contrib import admin
from .models import FavoritePlaylist, FollowArtist, FavoriteAlbum, FavoriteSong

admin.site.register(FavoritePlaylist)
admin.site.register(FollowArtist)
admin.site.register(FavoriteAlbum)
admin.site.register(FavoriteSong)