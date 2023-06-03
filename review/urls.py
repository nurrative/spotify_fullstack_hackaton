from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AddRatingAPIView, toggle_like, CommentViewSet

router = DefaultRouter()
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('rating/', AddRatingAPIView.as_view()),
    path('like/<int:id>/', toggle_like),

]