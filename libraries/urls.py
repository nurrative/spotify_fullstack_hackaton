from django.urls import path, include
from .views import FavoriteSongAPIView, FavoriteAlbumAPIView

urlpatterns = [
    path('songs/', FavoriteSongAPIView.as_view()),
    path('albums/', FavoriteAlbumAPIView.as_view()),

]