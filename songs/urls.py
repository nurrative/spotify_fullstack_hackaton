from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('artists', ArtistViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', SongListView.as_view()),
    path('songs/upload/', SongUploadView.as_view()),
    path('songs/<int:pk>/', SongRetrieveUpdateDestroyView.as_view()),
]