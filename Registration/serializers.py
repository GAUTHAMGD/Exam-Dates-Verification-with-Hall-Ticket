# external imports
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# local imports
from .models import User


class AuthUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=20, validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(max_length=256, write_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    last_login_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        instance = User.objects.create(**validated_data)
        return instance