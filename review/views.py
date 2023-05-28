from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import get_object_or_404

from playlists.models import Playlist
from .permissions import IsAuthor
from .models import Rating, Favorite, Like
from .serializers import RatingSerializer, FavoriteSerializer
# Create your views here.

# class FavoriteViewSet(
#     mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin,mixins.RetrieveModelMixin, GenericViewSet):
#     queryset =  Favorite.objects.all()
#     serializer_class = FavoriteSerializer
#     permission_classes = [IsAuthenticated, IsAuthor]
class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    lookup_field = 'id'
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
        #пытаемся установить фильтр по Избранным



class AddRatingAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=RatingSerializer())
    def post(self, request):
        ser = RatingSerializer(data=request.data, context={'request': request})
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status=201)

@api_view(['POST'])
def toggle_like(request, id):
    user = request.user
    if not user.is_authenticated:
        return Response(status=401)
    playlist = get_object_or_404(Playlist, id=id)
    if Like.objects.filter(user=user, playlist=playlist).exists():
        # Если лайк есть, то удаляем его
        Like.objects.filter(user=user, playlist=playlist).delete()
    else:
        # если нет, создаем
        Like.objects.create(user=user, playlist=playlist)
    return Response(status=201)