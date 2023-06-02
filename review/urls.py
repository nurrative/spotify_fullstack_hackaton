from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AddRatingAPIView #CommentViewSet

urlpatterns = [
    path('rating/', AddRatingAPIView.as_view()),

]