from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthor
from .models import *
from .serializers import PlaylistSerializer

class PlaylistListRetrieveView(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('title', 'description')
    permission_classes = [IsAuthenticated]

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('title', 'description')
    permission_classes = [IsAuthor, IsAuthenticated]