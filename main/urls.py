from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from . import views
from .views import TrackViewSet, ArtistViewSet

router = DefaultRouter()
router.register('tracks', TrackViewSet)
router.register('artists', ArtistViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('audio', views.Audio_store)
]