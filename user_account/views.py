from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .serializers import RegisterUserSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .serializers import *

User = get_user_model()


class RegisterUserView(APIView):
    @swagger_auto_schema(request_body=RegisterUserSerializer())
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Вы успешно зарегестрировались!", status=201)


class ActivationView(APIView):
    def get(self, request, activation_code):
        User = get_user_model()
        user = get_object_or_404(User, activation_code=activation_code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response("Ваш аккаунт успешно активирован!")


# class ChangePasswordAPIView(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     @swagger_auto_schema(request_body=ChangePasswordSerializer)
#     def post(self, request, *args, **kwargs):
#         current_password = request.data.get("current_password")
#         new_password = request.data.get("new_password")
#         confirm_password = request.data.get("confirm_password")
#
#         # Check if the current password is correct
#         if not request.user.check_password(current_password):
#             return Response({"message": "Current password is incorrect"}, status=400)
#
#         # Check if the new password and confirm password match
#         if new_password != confirm_password:
#             return Response({"message": "New password and confirm password do not match"}, status=400)
#
#         # Change the password and save the user
#         request.user.set_password(new_password)
#         request.user.save()
#
#         return Response({"message": "Password changed successfully"}, status=200)