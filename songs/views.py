from django.shortcuts import render

# Create your views here.
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SongSerializer
from .models import Song
from rest_framework.generics import ListAPIView
from drf_yasg.utils import swagger_auto_schema

class SongUploadView(APIView):
    parser_classes = [MultiPartParser]

    @swagger_auto_schema()
    def post(self, request, format=None):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



class SongListView(ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
