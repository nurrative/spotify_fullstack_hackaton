from rest_framework import serializers
from .models import Song, Artist, Album #Genre


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('title','artist', 'genre', 'release', 'description', 'cover_photo')

class ArtistSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True)

    songs = serializers.SerializerMethodField()

    class Meta:
        model = Artist
        fields = ('full_name', 'bio', 'albums', 'songs', 'photo')

    def get_songs(self, instance : Artist):
        songs = Song.objects.filter(album=instance)
        song_serializer = SongSerializer(songs, many=True)
        return song_serializer.data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['albums'] = AlbumSerializer(instance.albums.all(), many=True).data
        representation['songs'] = self.get_songs(instance)
        return representation


class SongSerializer(serializers.ModelSerializer):
    artist = serializers.SerializerMethodField()
    release_date = serializers.SerializerMethodField()
    cover_photo = serializers.SerializerMethodField()

    class Meta:
        model = Song
        fields = ('title', 'audio_file', 'album', 'artist', 'release_date', 'genre', 'cover_photo')

    def get_artist(self, obj):
        return obj.album.artist.full_name

    def get_release_date(self, obj):
        return obj.album.release
    
    def get_cover_photo(self,obj):
        return obj.album.cover_photo


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['artist'] = self.get_artist(instance)
        representation['release_date'] = self.get_release_date(instance)
        representation['cover_photo'] = self.get_cover_photo(instance)
        return representation
    

# class GenreSerializer(serializers.ModelSerializer):
#     songs = SongSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Genre
#         fields = ('slug', 'name', 'songs')