from django.contrib.auth import authenticate
from django.core.cache import cache
from django.db import transaction
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import User
from users.serializer import SignupSerializer, SigninSerializer
from rest_framework_simplejwt.views import TokenRefreshView
import jwt


class Signup(APIView):
    permission_classes = [AllowAny]

    @transaction.atomic
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "register successs",
                    "access": access_token,
                    "refresh_token": refresh_token,
                },
                status=status.HTTP_201_CREATED,
            )

            return res
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Signin(APIView):
    permission_classes = [AllowAny]

    @transaction.atomic
    def post(self, request):
        user = authenticate(
            email=request.data.get("email"), password=request.data.get("password")
        )
        if user is not None:
            # user_data = User.objects.get(email=request.data.get("email"))
            serializer = SigninSerializer(user)
            if user.is_delete:
                token = TokenObtainPairSerializer.get_token(user)
                refresh_token = str(token)
                access_token = str(token.access_token)
                res = Response(
                    {
                        "user": serializer.data,
                        "message": "login success",
                        "access": access_token,
                        "refresh_token": refresh_token,
                    },
                    status=status.HTTP_200_OK,
                )
                return res
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
