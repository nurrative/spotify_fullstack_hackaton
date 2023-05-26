from django.db import models

class Artist(models.Model):
    full_name = models.CharField(max_length=200)
    bio = models.TextField()
    photo = models.ImageField(upload_to='artist_photos', blank=True, null=True)

    def __str__(self):
        return self.full_name


class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    # genre = models.ManyToManyField(Genre, related_name='albums')
    release = models.DateField(auto_now_add=True)
    description = models.TextField()
    cover_photo = models.ImageField(upload_to='album_covers', blank=True, null=True)

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='songs')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
# class Genre(models.Model):
#     slug = models.SlugField(max_length=50, primary_key=True, unique=True)
#     name = models.CharField(max_length=50, unique=True)
#     # album = models.ManyToManyField('songs.Album', related_name='genres')
    # cover_song = models.ImageField(upload_to='media/songs/cover_songs', blank=True, null=True)

# from django.db import models
#
#
# class Album(models.Model):
#     title = models.CharField(max_length=100)
#     # artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
#     # genre = models.ManyToManyField(Genre, related_name='albums')
#     release = models.DateField(auto_now_add=True)
#     description = models.TextField()
#     cover_photo = models.ImageField(upload_to='media/album_covers/', blank=True, null=True)
#
#     def __str__(self):
#         return self.title
#
# class Song(models.Model):
#     title = models.CharField(max_length=100)
#     audio_file = models.FileField(upload_to='media/songs/')
#     album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
#     # genre = models.ForeignKey(Genre, models.CASCADE, related_name='songs')
#
#     def __str__(self):
#         return self.title
# class Artist(models.Model):
#     full_name = models.CharField(max_length=200)
#     bio = models.TextField()
#     album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='artists')
#     photo = models.ImageField(upload_to='media/artist_photos/', blank=True, null=True)
#     song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='artists')
#
#     def __str__(self):
#         return self.full_name
#
#     # @property
#     # def get_songs(self):
#     #     songs = self.ratings.all()  # так как ratings связан с продуктом через fk, то можем ссылаться на их related name
#     #     if ratings.exists():
#     #         return sum([x.value for x in ratings]) // ratings.count()
#     #         # ищем среднее значение рейтинга
#     #     return 0
#
#
# # class Genre(models.Model):
# #     slug = models.SlugField(max_length=50, primary_key=True, unique=True)
# #     name = models.CharField(max_length=50, unique=True)
# #     # album = models.ManyToManyField('songs.Album', related_name='genres')
#
#
#
#
#
#
#
#
