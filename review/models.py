from django.db import models

from playlists.models import Playlist
from user_account.models import User
from songs.models import *



# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='comments')
#     song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='comments')
#     body = models.TextField()
#     created_ad = models.DateTimeField(auto_now_add=True)
#     updated_ad = models.DateTimeField(auto_now=True)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name='ratings')
    value = models.IntegerField(choices=[(1,1),(2,2), (3,3), (4,4), (5,5)])
    #choices позволяет сократить выбор, можно выбрать только те значения, которые внутри choices

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='favorites')
    # album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='favorites')

class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    playlist = models.ForeignKey(Playlist, related_name='likes', on_delete=models.CASCADE)


