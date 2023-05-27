from django.db import models
from songs.models import Song
from user_account.models import User


class Playlist(models.Model):
    title = models.CharField(max_length=100)
    cover_photo = models.ImageField(upload_to='playlist_covers', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')
    # song = models.ManyToManyField(Song, related_name='playlists')
    song = models.ManyToManyField(Song, related_name='playlists')
    description = models.TextField()
