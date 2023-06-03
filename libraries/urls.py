from django.urls import path
from .views import FavoriteSongAPIView, FavoriteAlbumAPIView, FavoritePlaylistAPIView, FollowArtistAPIView


urlpatterns = [
    path('songs/', FavoriteSongAPIView.as_view()),
    path('albums/', FavoriteAlbumAPIView.as_view()),
    path('playlists/', FavoritePlaylistAPIView.as_view()),
    path('artists/', FollowArtistAPIView.as_view()),

]