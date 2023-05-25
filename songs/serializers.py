from rest_framework import serializers
from .models import Song, Artist, Genre, Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('title','artist', 'genre', 'release', 'description', 'cover_photo')

class ArtistSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ('full_name', 'bio', 'albums')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['albums'] = AlbumSerializer(instance.albums.all(), many=True).data
        return representation


class SongSerializer(serializers.ModelSerializer):
    artist = serializers.SerializerMethodField()
    release_date = serializers.SerializerMethodField()

    class Meta:
        model = Song
        fields = ('title', 'audio_file', 'album', 'artist', 'release_date', 'genre')

    def get_artist(self, obj):
        return obj.album.artist_id.full_name

    def get_release_date(self, obj):
        return obj.album.release

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['artist'] = self.get_artist(instance)
        representation['release_date'] = self.get_release_date(instance)
        return representation
    

class GenreSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = ('slug', 'name', 'songs')