from rest_framework.serializers import ModelSerializer
from .models import *

class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        exclude = ('user',)

    def validate(self, attrs):
        super().validate(attrs)
        attrs['user'] = self.context['request'].user
        return  attrs

    def create(self, validated_data): #хотим обновлять иди создавать новый рейтинг
        value = validated_data.pop('value')
        obj, created = Rating.objects.update_or_create(**validated_data, defaults={'value': value})
        return obj

    def to_representation(self, instance: Favorite):
        from playlists.serializers import PlaylistSerializer

        rep = super().to_representation(instance)
        rep['playlist'] = PlaylistSerializer(instance.song).data
        return  rep

class FavoriteSerializer(ModelSerializer):
    class Meta:
        model = Favorite
        exclude = ('user',)

    def validate(self, attrs):
        super().validate(attrs)
        attrs['user'] = self.context['request'].user
        return attrs

    def to_representation(self, instance: Favorite):
        from songs.serializers import SongSerializer

        rep = super().to_representation(instance)
        rep['song'] = SongSerializer(instance.song).data
        return  rep