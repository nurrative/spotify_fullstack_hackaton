from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from .serializers import RegisterUserSerializer, ChangePasswordSerializer,\
    PasswordResetSerializer,LogoutSerializer, ProfileSerializer
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView

class RegisterUserView(APIView):
    @swagger_auto_schema(request_body=RegisterUserSerializer())
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Проверьте вашу почту для аутентификации", status=201)
    

User = get_user_model()


@api_view(["GET"])
def activate(request, activation_code):
    user = get_object_or_404(User, activation_code=activation_code)
    user.is_active = True
    user.activation_code = ''
    user.save()
    return redirect("http://127.0.0.1:3000/")


class ChangePasswordAPIView(APIView):
    '''
    Only authorized users can change the password
    '''
    permission_classes = (IsAuthenticated,)
    @swagger_auto_schema(request_body=ChangePasswordSerializer)
    def post(self, request, *args, **kwargs):
        current_password = request.data.get("current_password")
        new_password = request.data.get("new_password")
        confirm_password = request.data.get("confirm_password")

        if not request.user.check_password(current_password):
            return Response({"message": "Current password is incorrect"}, status=400)

        if new_password != confirm_password:
            return Response({"message": "New password and confirm password do not match"}, status=400)

        request.user.set_password(new_password)
        request.user.save()

        return Response({"message": "Password changed successfully"}, status=200)


class PasswordResetView(CreateAPIView):
    serializer_class = PasswordResetSerializer


class LogoutAPIView(APIView):
    '''
    Only authorized users can make a logout
    '''
    permission_classes = (IsAuthenticated,)
    serializer_class = [LogoutSerializer,]
    @swagger_auto_schema(request_body=LogoutSerializer)
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=204)
        except Exception as e:
            return Response(status=400)

class ProfileViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer


class CustomTokenRefreshView(TokenRefreshView):

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
