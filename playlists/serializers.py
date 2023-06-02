from rest_framework.serializers import ModelSerializer

from review.serializers import CommentSerializer
from .models import *
from songs.serializers import SongSerializer


class PlaylistSerializer(ModelSerializer):
    song = SongSerializer(many=True, read_only=True)  # Используем SongSerializer для ManyToMany-поля
    comments = CommentSerializer(many=True, read_only=True)

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
        # rep['comments'] = instance.comments.all()
        return rep




# class LibrarySerializer(ModelSerializer):
#     model = Library
#     exclude = ('user',)
#     rep['user'] = {
#         'id': instance.user.id,
#         'email': instance.user.email,
#     }