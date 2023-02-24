from rest_framework import serializers
from .models import history


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
        fields = ['history_id', 'is_spend', 'memo', 'cost', 'balance', 'created_at', 'updated_at']


class history_serializer(serializers.ModelSerializer):
    class Meta:
        model = history
        fields = '__all__'
