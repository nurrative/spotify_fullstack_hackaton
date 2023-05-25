from rest_framework import serializers
from .models import Song, Artist

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'  #('id', 'title', 'audio_file')

 # title = models.CharField(max_length=100)
 #    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
 #    audio_file = models.FileField(upload_to='songs/')
 #    album_id = models.CharField(max_length=50)
 #    release = models.DateField(auto_now_add=True)
 #    genre = models.CharField(max_length=50)

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        # exclude = ('user',)
        fields = '__all__'

    def to_representation(self, instance: Artist):
        rep = super().to_representation(instance)
        rep['song'] = SongSerializer(instance.song).data
        return  rep