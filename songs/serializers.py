from rest_framework import serializers
from .models import Song, Artist, Album  # Genre
from django.utils.encoding import force_str


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id','title', 'artist', 'release', 'description', 'cover_photo')


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
        fields = ('id','title', 'audio_file', 'album', 'artist', 'release_date', 'cover_photo') #cover_song

    def get_artist(self, obj):
        return obj.album.artist.full_name

    def get_release_date(self, obj):
        return obj.album.release



    # def get_cover_photo(self, obj):
    #     request = self.context.get('request')
    #     if obj.album.cover_photo:
    #         return request.build_absolute_uri(obj.album.cover_photo.url)
    #     return None

    def get_cover_photo(self, obj):
        # return force_str(obj.album.cover_photo)
        return f'http://127.0.0.1:8000/{force_str(obj.album.cover_photo)}'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['artist'] = self.get_artist(instance)
        representation['release_date'] = self.get_release_date(instance)
        representation['cover_photo'] = self.get_cover_photo(instance)
        return representation