from django.db import models


class Artist(models.Model):
    full_name = models.CharField(max_length=200)
    albums = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return self.full_name
class Song(models.Model):
    title = models.CharField(max_length=100)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
    audio_file = models.FileField(upload_to='songs/')
    album = models.CharField(max_length=50, )
    release = models.DateField(auto_now_add=True)
    # genre = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    # def validate(self, attrs):
    #     # но нам нужно добавить поле user в наш словарь с данными, поэтому переопределяем функцию validate
    #     super().validate(attrs)
    #     attrs['artist'] = self.context['request'].user
    #     return attrs

    # def to_representation(self, instance):
    #     #хотим внести доп инфу в блок user
    #     rep = super().to_representation(instance)
    #     rep['artist'] = {
    #         'artist_id': instance.artist.id,
    #     }
    #     return rep
