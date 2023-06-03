from .permissions import IsAuthor
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import FavoriteSongSerializer, FavoriteAlbumSerializer, \
    FollowArtistSerializer, FavoritePlaylistSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response


class FavoriteSongAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAuthor]

    def get(self, request):
        user_id = request.user.id
        favorites = FavoriteSong.objects.filter(user=user_id)
        serializer = FavoriteSongSerializer(favorites, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=FavoriteSongSerializer)
    def post(self, request):
        user_id = request.user.id
        favorite_song = FavoriteSong.objects.filter(user=user_id, songs=request.data.get('songs')).first()

        if favorite_song:

            favorite_song.delete()
            return Response(status=204)

        serializer = FavoriteSongSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class FavoriteAlbumAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAuthor]

    def get(self, request):
        user_id = request.user.id
        favorites = FavoriteAlbum.objects.filter(user=user_id)
        serializer = FavoriteAlbumSerializer(favorites, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=FavoriteAlbumSerializer)
    def post(self, request):
        user_id = request.user.id
        favorite_album = FavoriteAlbum.objects.filter(user=user_id, albums=request.data.get('albums')).first()

        if favorite_album:
            favorite_album.delete()
            return Response(status=204)

        serializer = FavoriteAlbumSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class FavoritePlaylistAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAuthor]

    def get(self, request):
        user_id = request.user.id
        favorites = FavoritePlaylist.objects.filter(user=user_id)
        serializer = FavoritePlaylistSerializer(favorites, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=FavoritePlaylistSerializer)
    def post(self, request):
        user_id = request.user.id
        favorite_playlist = FavoritePlaylist.objects.filter(user=user_id, playlist=request.data.get('playlists')).first()

        if favorite_playlist:
            favorite_playlist.delete()
            return Response(status=204)

        serializer = FavoritePlaylistSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class FollowArtistAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAuthor]

    def get(self, request):
        user_id = request.user.id
        favorites = FollowArtist.objects.filter(user=user_id)
        serializer = FollowArtistSerializer(favorites, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=FollowArtistSerializer)
    def post(self, request):
        user_id = request.user.id
        follow_artist = FollowArtist.objects.filter(user=user_id, artists=request.data.get('artists')).first()

        if follow_artist:
            follow_artist.delete()
            return Response(status=204)

        serializer = FollowArtistSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


