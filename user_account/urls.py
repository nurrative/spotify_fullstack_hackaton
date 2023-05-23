from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import  *

urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('activate/<str:activation_code>/', ActivationView.as_view()),
    # path('change_password/', ChangePasswordAPIView.as_view()),
]