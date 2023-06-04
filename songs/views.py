from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .serializers import *
from .models import *
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from .permission import IsAdminOrReadOnly

class SongUploadView(APIView):
    parser_classes = [MultiPartParser]

    @swagger_auto_schema(request_body=SongSerializer)
    def post(self, request, format=None):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class SongListView(ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filterset_fields = ('genre',)
    search_fields = ('title',)

class SongRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsAdminOrReadOnly]


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend,)
    search_fields = ('full_name',)
    permission_classes = [IsAdminOrReadOnly]


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('title',)
    permission_classes = [IsAdminOrReadOnly]

class GenreListView(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [AllowAny, ]


@api_view(["GET"])
def show_similar_songs(request, pk):
    """
    Shows songs in the same genre
    """
    genre = get_object_or_404(Genre, slug=pk)
    relative_songs = Song.objects.filter(genre=genre)
    song_serializer = SongSerializer(relative_songs, many=True)
    data = song_serializer.data
    # data = data[]
    data = [{**song, 'audio_file': f"{config('LINK')}{song['audio_file']}"} for song in data]
    similar_songs_url = reverse('similar_songs', args=[pk])
    # print(data[genre])
    # print(song_serializer.data)

    return Response({
        'similar_songs': data,
        #similar_songs_url': similar_songs_url,
    })

 # def get_songs(self, instance: Artist):
 #        albums = instance.albums.all()
 #        songs = Song.objects.filter(album__in=albums)
 #        song_serializer = SongSerializer(songs, many=True)
 #        data = song_serializer.data
 #        data = [{**song, 'audio_file': f"{config('LINK')}{song['audio_file']}"} for song in data]
 #        return data








