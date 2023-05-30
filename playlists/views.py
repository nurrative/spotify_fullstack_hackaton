from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthor
from .models import *
from .serializers import PlaylistSerializer
# Create your views here.

# class PlaylistViewSet(
#     mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin,mixins.RetrieveModelMixin, GenericViewSet):
#     queryset =  Favorite.objects.all()
#     serializer_class = FavoriteSerializer
#

# class PlaylistViewSet(viewsets.ModelViewSet):
#     queryset = Playlist.objects.all()
#     serializer_class = PlaylistSerializer
    # permission_classes = [IsAuthenticated, IsAuthor]

class PlaylistListRetrieveView(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    # filterset_fields = ('playlists_rating',)
    search_fields = ('title', 'description')
    permission_classes = [IsAuthenticated]

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    # filterset_fields = ('playlists_rating',)
    search_fields = ('title', 'description')
    permission_classes = [IsAuthor, IsAuthenticated] #