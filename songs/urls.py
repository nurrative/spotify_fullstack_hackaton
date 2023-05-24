from django.urls import path
from .views import *

urlpatterns = [
    path('', SongListView.as_view()),
    path('upload/', SongUploadView.as_view()),
]