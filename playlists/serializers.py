from rest_framework.serializers import ModelSerializer
from .models import *
from songs.serializers import SongSerializer


class PlaylistSerializer(ModelSerializer):
    song = SongSerializer(many=True)  # Используем SongSerializer для ManyToMany-поля

    class Meta:
        model = Playlist
        exclude = ('user',)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['user'] = {
            'id': instance.user.id,
            'email': instance.user.email,
        }
        rep['likes'] = instance.likes.all().count()
        rep['rating'] = instance.average_rating
        return rep


# class LibrarySerializer(ModelSerializer):
#     model = Library
#     exclude = ('user',)
#     rep['user'] = {
#         'id': instance.user.id,
#         'email': instance.user.email,
#     }