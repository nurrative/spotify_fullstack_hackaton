from django.db import models

# Create your models here.

class Artist(models.Model):
    full_name = models.CharField(max_length=200)
    albums = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return self.full_name

# class Audio_store(models.Model):
#     record = models.FileField(upload_to='documents/')
#     class Meta:
#         db_table = 'Audio_store'


class Track(models.Model):
    title = models.CharField(max_length=100)
    artist_id = models.ForeignKey(Artist,  on_delete=models.CASCADE,related_name='tracks')
    # file = models.FileField(upload_to='uploads/', null=True, blank=True)
    album = models.CharField(max_length=100)
    release = models.DateField(auto_now_add = True)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class SongFile(models.Model):
    objects = None
    song = models.FileField(upload_to='songs/', blank=True,null=True)
    track = models.ForeignKey(Track,on_delete=models.CASCADE,related_name='songs')