from rest_framework.serializers import ModelSerializer
from .models import *
from songs.serializers import SongSerializer
from review.serializers import CommentSerializer


class PlaylistSerializer(ModelSerializer):
    # song = SimpleSongSerializer(many=True) #read_only=True
    #
    # Используем SongSerializer для ManyToMany-поля


    class Meta:
        model = Playlist
        exclude = ('user', 'song')

    def validate(self, attrs):
        super().validate(attrs)
        attrs['user'] = self.context['request'].user
        return attrs

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['user'] = {
            'id': instance.user.id,
            'email': instance.user.email,
        }
        rep['likes'] = instance.likes.all().count()
        rep['rating'] = instance.average_rating
        rep['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        rep['songs'] = SongSerializer(instance.song.all(), many=True).data
        return rep


class SimplePlaylist(ModelSerializer):
    class Meta:
        model = Playlist
        fields = ('id', 'title', 'cover_photo')
