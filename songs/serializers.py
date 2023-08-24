
from rest_framework import serializers
from .models import *
from django.utils.encoding import force_str
from decouple import config
from drf_writable_nested import WritableNestedModelSerializer


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
        fields = ('id', 'full_name', 'bio', 'albums', 'songs', 'photo')

    def get_songs(self, instance: Artist):
        albums = instance.albums.all()
        songs = Song.objects.filter(album__in=albums)
        song_serializer = SimpleSongSerializer(songs, many=True).data
        # data = song_serializer.data
        # data = [{**song, 'audio_file': f"{config('LINK')}{song['audio_file']}"} for song in data]
        return song_serializer

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['songs'] = self.get_songs(instance)
        return representation


class SongSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    artist = serializers.SerializerMethodField()
    release_date = serializers.SerializerMethodField()
    cover_photo = serializers.SerializerMethodField()


    class Meta:
        model = Song
        fields = ('id','title', 'audio_file','genre', 'album', 'artist', 'release_date','cover_photo') #'cover_photo'

    def get_artist(self, obj):
        return {'id': obj.album.artist.id, 'title': obj.album.artist.full_name}

    def get_release_date(self, obj):
        return obj.album.release


    def get_cover_photo(self, obj):
        return f'{config("LINK")}{force_str(obj.album.cover_photo)}'


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['artist'] = self.get_artist(instance)
        representation['release_date'] = self.get_release_date(instance)
        representation['cover_photo'] = self.get_cover_photo(instance)
        representation['genre'] = GenreSerializer(instance.genre).data
        # representation['songs'] = SimpleAlbumSerializer(instance.album).data
        # for album_data in albums_data:
        #     album_data['cover_photo'] = f"{config('LINK')}{album_data['cover_photo']}"
        # representation['songs'] = albums_data
        return representation


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id','title','artist', 'release', 'description', 'cover_photo',) #'songs'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['songs'] = SimpleSongSerializer(instance.songs.all(), many=True).data
        # for song_data in songs_data:
        #     song_data['audio_file'] = f"{config('LINK')}{song_data['audio_file']}"
        # representation['songs'] = songs_data
        return representation


class SimpleArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('id', 'full_name', 'photo')


class SimpleSongSerializer(serializers.ModelSerializer):
    release_date = serializers.SerializerMethodField()
    cover_photo = serializers.SerializerMethodField()

    class Meta:
        model = Song
        fields = ('id', 'title', 'audio_file', 'release_date','cover_photo')

    def get_release_date(self, obj):
        return obj.album.release


    def get_cover_photo(self, obj):
        return f'{config("LINK")}{force_str(obj.album.cover_photo)}'

def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['audio_file'] = f"{config('LINK')}{rep['audio_file']}"
        rep['release_date'] = self.get_release_date(instance)
        rep['cover_photo'] = self.get_cover_photo(instance)
        return rep
...
