from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings
from .views import *

router = DefaultRouter()
router.register('playlist/user', PlaylistListRetrieveView, basename='playlist-user')
router.register('playlist/author', PlaylistViewSet, basename='playlist-author')


urlpatterns = [
    path('', include(router.urls)),
]