from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class SigninSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = User(
            email=email,
        )
        user.set_password(password)
        user.save()
        return user
