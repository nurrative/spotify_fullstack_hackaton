from django.db import models


class Artist(models.Model):
    full_name = models.CharField(max_length=200)
    # album = models.CharField(max_length=200)
    bio = models.TextField()
    ''' album = models.ForeignKey(Albums, on_delete=models.CASCADE, related_name='albums') - 
        в to representation укажем все это'''

    def __str__(self):
        return self.full_name
class Song(models.Model):
    title = models.CharField(max_length=100)
    # album_id = models.ForeignKey(Albums, on_delete=models.CASCADE, related_name='songs')
    audio_file = models.FileField(upload_to='songs/')
    # album = models.CharField(max_length=50, )
    ''' 1) release_album = models.ForeignKey(Albums, on_delete=models.CASCADE, related_name='albums') - 
    2) + album_id 
    
    в to representation укажем все это'''

    # genre = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Albums(models.Model):
    title = models.CharField(max_length=100)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='albums')
    release = models.DateField(auto_now_add=True)
    description = models.TextField()

