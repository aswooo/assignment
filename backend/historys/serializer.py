from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import history
from users.models import User


class save_serializer(serializers.ModelSerializer):
    class Meta:
        model = history
        fields = ['is_spend', 'cost', 'memo', 'fk_user', 'balance']

class get_all_serializer(serializers.ModelSerializer):
    class Meta:
        model = history
        fields = ['history_id', 'is_spend', 'cost', 'balance', 'created_at']


class get_history_serializer(serializers.ModelSerializer):
    class Meta:
        model = history
        fields = ['history_id', 'is_spend', 'memo', 'cost', 'balance', 'created_at', 'update_at']


class history_serializer(serializers.ModelSerializer):
    class Meta:
        model = history
        fields = '__all__'
