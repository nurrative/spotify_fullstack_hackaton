from rest_framework import serializers
from .models import Song, Artist, Album  # Genre
from django.utils.encoding import force_str
from decouple import config

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id','title','artist', 'release', 'description', 'cover_photo')

class ArtistSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True)
    songs = serializers.SerializerMethodField()

    class Meta:
        model = Artist
        fields = ('id','full_name', 'bio', 'albums', 'songs', 'photo')

    def get_songs(self, instance: Artist):
        albums = instance.albums.all()
        songs = Song.objects.filter(album__in=albums)
        song_serializer = SongSerializer(songs, many=True)
        # print(song_serializer.data)
        data = song_serializer.data
        data = [{**song, 'audio_file': f"{config('LINK')}{song['audio_file']}"} for song in data]
        # print(data)
        return data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['albums'] = AlbumSerializer(instance.albums.all(), many=True).data
        print(representation['albums'])
        # representation['albums'] = [**rep]
        representation['songs'] = self.get_songs(instance)
        return representation


class SongSerializer(serializers.ModelSerializer):
    artist = serializers.SerializerMethodField()
    release_date = serializers.SerializerMethodField()
    cover_photo = serializers.SerializerMethodField()

    class Meta:
        model = Song
        fields = ('id','title', 'audio_file', 'album', 'artist', 'release_date', 'cover_photo') #cover_song

    def get_artist(self, obj):
        return obj.album.artist.id, obj.album.artist.full_name

    def get_release_date(self, obj):
        return obj.album.release


    def get_cover_photo(self, obj):
        return f'{config("LINK")}/media/{force_str(obj.album.cover_photo)}'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['artist'] = self.get_artist(instance)
        representation['release_date'] = self.get_release_date(instance)
        representation['cover_photo'] = self.get_cover_photo(instance)
        return representation