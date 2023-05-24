from rest_framework import serializers
from .models import Track, SongFile, Artist

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        # exclude = ('user',)
        fields = '__all__'
class TrackSerializer(serializers.ModelSerializer):
    release = serializers.DateField(format='%d/%m/%Y', read_only=True)
    #чтобы по умолчанию он заполнялся
    class Meta:
        model = Track
        fields = '__all__'
        #чисто для себя прописываем, какие поля должны сереализоваться

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        #representation содержит весь словарь формата json
        representation['songs'] = SongFileSerializer(instance.songs.all(),
                                                       many=True,context=self.context).data
        #создаем поле images в словаре
        return representation

    # def create(self, validated_data):
    #     request = self.context.get('request')
    #     user_id = request.user.id
    #     validated_data['author_id'] = user_id
    #     post = Post.objects.create(**validated_data)
    #     return post

class SongFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongFile
        fields = '__all__'

    def _get_image_url(self, obj):
        # чтобы сслыка на изображение перекидывалаа на саму фотографию создаем данный метод
        if obj.image: # если есть изображение, то сработает код ниже
            url = obj.image.url #????
            request = self.context.get('request')
            #context содержит в себе словарь со всеми данными
            # из него вытаскиваем значения по ключу request, который мы создали в serializer
            if request is not None:
                url = request.build_absolute_uri(url) #
            else:
                url = ''
            return  url

    def to_representation(self, instance):
        #instance - объект PostImage
        representation = super().to_representation(instance)
        representation['song'] = self._get_image_url(instance)
        return representation
