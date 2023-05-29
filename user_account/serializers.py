from rest_framework import serializers
from django.utils.crypto import get_random_string
from .models import UserImage, User
from .utils import send_activation_code, reset_password
from review.serializers import *
from playlists.serializers import *


class RegisterUserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(min_length=4, required=True)

    class Meta:
        model = User
        fields = ('email', 'phone', 'password', 'password_confirm')

    def validate(self, attrs):
        # ATTRS BEFORE -> OrderedDict([('email', 'admin1@gmail.com'), ('phone', '996700071102'), ('password', '12345'), ('password_confirm', '12345')])
        pass1 = attrs.get("password")
        pass2 = attrs.pop("password_confirm")
        # ATTRS AFTER POP -> # ATTRS -> OrderedDict([('email', 'admin1@gmail.com'), ('phone', '996700071102'), ('password', '12345')])
        if pass1 != pass2:
            raise serializers.ValidationError("Пароли не совпадают!")
        return attrs

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Пользователь с такой почтой уже существует!")
        return email

    def validate_phone(self, phone):
        print('Введите номер телефона: +996 ... ... ...')
        if phone.startswith('+996') == False:
            raise serializers.ValidationError("Номер телефона должен начинаться с +996")
        if len(phone) != 13:
            raise serializers.ValidationError(
                "Неправильно введён номер телефона! Проверьте, пожалуйста, внесённые вами данные.")
        return phone


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        send_activation_code(email=user.email, activation_code=user.activation_code)
        return user


class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserImage
        fields = '__all__'

    def _get_image_url(self, obj):
        # чтобы сслыка на изображение перекидывалаа на саму фотографию создаем данный метод
        if obj.image:  # если есть изображение, то сработает код ниже
            url = obj.image.url  # ????
            request = self.context.get('request')
            # context содержит в себе словарь со всеми данными
            # из него вытаскиваем значения по ключу request, который мы создали в serializer
            if request is not None:
                url = request.build_absolute_uri(url)  #
            else:
                url = ''
            return url

    def to_representation(self, instance):
        # instance - объект PostImage
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        return representation


class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate(self, data):
        """
        Проверяем, что новый пароль и подтверждение пароля совпадают
        """
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("The new password and confirmation do not match")
        return data

    def save(self):
        data = self.validated_data
        user = User.objects.get(email=data['email'])
        user.set_activation_code()
        user.password_confirm()

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        # Проверяем, существует ли пользователь с указанным email
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Пользователь с указанным email не существует.")
        return value

    def save(self):
        email = self.validated_data['email']
        user = User.objects.get(email=email)
        # Генерируем новый пароль
        new_password = get_random_string(length=8)
        # Устанавливаем новый пароль для пользователя
        user.set_password(new_password)
        user.save()
        # Отправляем email с новым паролем
        reset_password(email, new_password)

class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

class ProfileSerializer(serializers.ModelSerializer):
    # favorites = FavoriteSerializer(many=True, read_only=True)
    # playlists = PlaylistSerializer(many=True, read_only=True)
    # ratings = RatingSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('email', 'phone' ) #'ratings' 'playlists', favorites

    # def get_artist(self, obj):
    #     return obj.album.artist.full_name
    #
    # def to_representation(self, instance: User):
    #     #self - это обекты от ProfileSerializer
    #     #instance - это обекты от User. Его получим после того как нам передадут аргумент
    #     rep = super().to_representation(instance)
    #     #собирает словарь из fields = ('email', 'phone', 'bio')
    #     rep['favourite'] = instance.favourites.song
    #     return rep

