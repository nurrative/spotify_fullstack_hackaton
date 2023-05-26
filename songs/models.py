from django.db import models


class Artist(models.Model):
    full_name = models.CharField(max_length=200)
    bio = models.TextField()
    photo = models.ImageField(upload_to='media/artist_photos/', blank=True, null=True)

    def __str__(self):
        return self.full_name
    

class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    # genre = models.ManyToManyField(Genre, related_name='albums')
    release = models.DateField(auto_now_add=True)
    description = models.TextField()
    cover_photo = models.ImageField(upload_to='media/album_covers/', blank=True, null=True)

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='media/songs/')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    # genre = models.ForeignKey(Genre, models.CASCADE, related_name='songs')

    def __str__(self):
        return self.title

# class Genre(models.Model):
#     slug = models.SlugField(max_length=50, primary_key=True, unique=True)
#     name = models.CharField(max_length=50, unique=True)
#     # album = models.ManyToManyField('songs.Album', related_name='genres')

