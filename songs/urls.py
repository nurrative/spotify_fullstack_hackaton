from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('albums', AlbumViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('songs/', SongListView.as_view()),
    path('songs/upload/', SongUploadView.as_view()),
    path('songs/<int:pk>/', SongRetrieveUpdateDestroyView.as_view()),
    path('artists/', ArtistListCreateAPIView.as_view()),
    path('artists/<int:id>/', ArtistRetrieveUpdateDestroyView.as_view())
]