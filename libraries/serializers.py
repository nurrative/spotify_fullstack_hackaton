from rest_framework.serializers import ModelSerializer
from .models import *
from decouple import config


class FavoriteSongSerializer(ModelSerializer):
    class Meta:
        model = FavoriteSong
        exclude = ('user',)

    def validate(self, attrs):
        super().validate(attrs)
        attrs['user'] = self.context['request'].user
        return attrs

    def to_representation(self, instance: FavoriteSong):
        from songs.serializers import SongSerializer
        rep = super().to_representation(instance)
        song_data = SongSerializer(instance.songs).data
        audio_file = song_data['audio_file']
        audio_file = config("LINK") + audio_file
        song_data['audio_file'] = audio_file
        rep['songs'] = song_data
        return rep


class FavoriteAlbumSerializer(ModelSerializer):
    class Meta:
        model = FavoriteAlbum
        exclude = ('user',)

    def validate(self, attrs):
        super().validate(attrs)
        attrs['user'] = self.context['request'].user
        return attrs

    def to_representation(self, instance: FavoriteSong):
        from songs.serializers import SimpleAlbumSerializer
        rep = super().to_representation(instance)
        album_data = SimpleAlbumSerializer(instance.albums).data
        cover_photo = album_data['cover_photo']
        cover_photo = config("LINK")+cover_photo
        album_data['cover_photo'] = cover_photo
        rep['albums'] = album_data
        return rep

class FavoritePlaylistSerializer(ModelSerializer):
    class Meta:
        model = FavoritePlaylist
        exclude = ('user',)

    def validate(self, attrs):
        super().validate(attrs)
        attrs['user'] = self.context['request'].user
        return attrs

    def to_representation(self, instance: FavoritePlaylist):
        from playlists.serializers import SimplePlaylist
        rep = super().to_representation(instance)
        song_data = SimplePlaylist(instance.playlist).data
        # audio_file = song_data['audio_file']
        # audio_file = config("LINK") + audio_file
        # song_data['audio_file'] = audio_file
        # rep['songs'] = song_data
        playlist_data = SimplePlaylist(instance.playlist).data
        rep['playlists'] = playlist_data
        return rep


class FollowArtistSerializer(ModelSerializer):
    class Meta:
        model = FollowArtist
        exclude = ('user',)

    def validate(self, attrs):
        super().validate(attrs)
        attrs['user'] = self.context['request'].user
        return attrs

    def to_representation(self, instance: FollowArtist):
        from songs.serializers import SimpleArtistSerializer
        rep = super().to_representation(instance)
        artist_data = SimpleArtistSerializer(instance.artists).data
        rep['artists'] = artist_data
        return rep

