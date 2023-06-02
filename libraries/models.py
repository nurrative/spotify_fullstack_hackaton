from django.db import models
from user_account.models import User
from songs.models import *
from playlists.models import Playlist


class FavoriteSong(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_songs')
    songs = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='favorite_songs')


class FavoriteAlbum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_albums')
    albums = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='favorite_albums')


class FollowArtist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follow_artists')
    artists = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='follow_artists')


class FavoritePlaylist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_playlists')
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name='favorite_playlists')



