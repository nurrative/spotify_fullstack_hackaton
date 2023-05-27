from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FavoriteViewSet, AddRatingAPIView #CommentViewSet

router = DefaultRouter()
# router.register('comments', CommentViewSet
router.register('favorite', FavoriteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('rating/', AddRatingAPIView.as_view()),

]