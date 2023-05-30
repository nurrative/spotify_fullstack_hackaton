from rest_framework import serializers
from .models import *
from django.utils.encoding import force_str
from decouple import config


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class SimpleAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'title', 'cover_photo')

class ArtistSerializer(serializers.ModelSerializer):
    albums = SimpleAlbumSerializer(many=True, read_only=True)
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
        # representation['albums'] = AlbumSerializer(instance.albums.all(), many=True).data
        # print(representation['albums'])
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
        representation['genre'] = GenreSerializer(instance.genre).data
        return representation


class AlbumSerializer(serializers.ModelSerializer):
    # songs = serializers.SongSerializer(many=True, read_only=True)
    class Meta:
        model = Album
        fields = ('id','title','artist', 'release', 'description', 'cover_photo', ) #'songs'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        songs_data = SongSerializer(instance.songs.all(), many=True).data
        for song_data in songs_data:
            song_data['audio_file'] = f"{config('LINK')}{song_data['audio_file']}"
        representation['songs'] = songs_data
        return representation

