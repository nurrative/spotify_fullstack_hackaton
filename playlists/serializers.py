from rest_framework.serializers import ModelSerializer
from .models import *
from songs.serializers import SongSerializer

# class PlaylistSerializer(ModelSerializer):
#     # songs = SimpleAlbumSerializer(many=True, read_only=True)
#     class Meta:
#         model = Playlist
#         exclude = ('user',)
# # def validate(self, attrs):
# #     super().validate(attrs)
# #     attrs['user'] = self.context['request'].user
# #     return attrs
#
# # def to_representation(self, instance: Playlist):
# #     from songs.serializers import SongSerializer
# #     rep = super().to_representation(instance)
# #     # rep['song'] = SongSerializer(instance.song).data
# #
# #     return rep
#
#     def to_representation(self, instance):
#         rep = super().to_representation(instance)
#         rep['user'] = {
#             'id': instance.user.id,
#             'email': instance.user.email,
#         }
#         rep['song'] = SongSerializer(instance.song).data
#         return  rep

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
        return rep


