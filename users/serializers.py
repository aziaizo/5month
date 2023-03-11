from rest_framework import serializers
from .models import User
from rest_framework.exceptions import ValidationError



class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()



class UserRegisterSerializer(UserLoginSerializer):
    @staticmethod
    def validate_username(username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('User already exists!')


