from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from historys.serializer import *
from rest_framework.permissions import IsAuthenticated


def search_user(request):
    jwt_object = JWTAuthentication()
    header = jwt_object.get_header(request)  # 헤더
    raw_token = jwt_object.get_raw_token(header)  # 원시 토큰
    validated_token = jwt_object.get_validated_token(raw_token)  # 검증된 토큰
    user = jwt_object.get_user(validated_token)  # 유저 객체
    return user


class History(APIView):
    permission_classes = ([IsAuthenticated])

    @transaction.atomic
    def post(self, request):
        user = search_user(request)
        if user is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        data = request.data
        data["balance"] = user.balacne
        data["fk_user"] = user.id
        if request.data.get("is_spend"):
            data["balance"] -= request.data["cost"]
            data["user_id_id"] = user.id
        else:
            data["balance"] += request.data["cost"]
        serializer = save_serializer(data=data)
        user = search_user(request)
        if serializer.is_valid():
            serializer.save()
            user.balacne = data["balance"]
            user.save()
        else:
            Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=201)


class Update_history(APIView):
    permission_classes = ([IsAuthenticated])

    def get(self, request, history_id):
        user = search_user(request)  # 토큰의 유효성 검사
        if user is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            data = history.objects.get(history_id=history_id)
            serializer = get_history_serializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @transaction.atomic
    def put(self, request, history_id):
        user = search_user(request)  # 토큰의 유효성 검사
        if user is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        origin = history.objects.get(history_id=history_id)  # 기존 객체 가져오기
        origin.memo = request.data["memo"]
        if request.data.get("is_spend"):
            balance = user.balance + origin.cost - request.data["cost"]
        else:
            balance = user.balance - origin.cost + request.data["cost"]
        origin.balance = balance
        user.balance = balance
        try:
            origin.save()
            user.save()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)

    @transaction.atomic
    def delete(self, request, history_id):
        user = search_user(request)
        if user is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            origin = history.objects.get(history_id=history_id)
            origin.is_deleted = True
            if request.data.get("is_spend"):
                user.balance += origin.balance
            else:
                user.balance -= origin.balance
            origin.save()
            user.save()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)
