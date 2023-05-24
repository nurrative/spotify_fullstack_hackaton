from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets
# from .forms import AudioForm
from .models import Track, SongFile, Artist
from .serializers import TrackSerializer, SongFileSerializer, ArtistSerializer

# def Audio_store(request):
#     if request.method == 'POST':
#         form = AudioForm(request.POST, request.FILES or None)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('successfully uploaded')
#         else:
#             form = AudioForm()
#         return render(request, 'aud.htm', {'form': form})

class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
