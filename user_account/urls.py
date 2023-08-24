from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import RegisterUserView, ProfileViewSet, activate, PasswordResetView, ChangePasswordAPIView, \
    LogoutAPIView, CustomTokenRefreshView

router = DefaultRouter()
router.register('profile', ProfileViewSet)

urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('password-reset/', PasswordResetView.as_view()),
    path('change_password/', ChangePasswordAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
    path('', include(router.urls)),
    path('refresh_token/', CustomTokenRefreshView.as_view()),


]