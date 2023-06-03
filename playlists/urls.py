from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlaylistViewSet, PlaylistListRetrieveView

router = DefaultRouter()
router.register('playlist/user', PlaylistListRetrieveView, basename='playlist-user')
router.register('playlist/author', PlaylistViewSet, basename='playlist-author')


urlpatterns = [
    path('', include(router.urls)),
]