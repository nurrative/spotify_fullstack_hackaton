from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings
from .views import *

router = DefaultRouter()
router.register('playlist', PlaylistViewSet)

urlpatterns = [
    path('', include(router.urls)),
]