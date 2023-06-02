from django.db import models
from songs.models import Song
from user_account.models import User


class Playlist(models.Model):
    title = models.CharField(max_length=100)
    cover_photo = models.ImageField(upload_to='playlist_covers', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')
    song = models.ManyToManyField(Song, related_name='playlists')
    description = models.TextField()

    @property
    def average_rating(self):
        ratings = self.ratings.all()  # так как ratings связан с продуктом через fk, то можем ссылаться на их related name
        if ratings.exists():
            return sum([x.value for x in ratings]) // ratings.count()
            # ищем среднее значение рейтинга
        return 0

    def __str__(self):
        return self.title

