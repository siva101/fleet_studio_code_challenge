from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django.core.exceptions import ValidationError

User = get_user_model()


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=8, required=True)
    password = serializers.CharField(max_length=6,required=True, write_only=True)


class AuthUserSerializer(serializers.ModelSerializer):
    auth_token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id','username', 'password', 'email', 'mobileno','auth_token')


    def get_auth_token(self, obj):
        try:
            token=Token.objects.get(user=obj)
        except Token.DoesNotExist:
            token = Token.objects.create(user=obj)
        return token.key


class EmptySerializer(serializers.Serializer):
    pass


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    A user serializer for registering the user
    """
    password = serializers.CharField(
        style={'input_type': 'password'}
    )
    class Meta:
        model = User
        fields = ('id','username', 'password','email','mobileno')

    def validate_username(self, value):

        user = User.objects.filter(username='username')
        if user:
            raise serializers.ValidationError("Username is already taken")
        return AbstractBaseUser.normalize_username(value)

    def validate_password(self, value):
        special_characters ="_-#"
        if not any(char.isdigit() for char in value):
            raise ValidationError("Password must contain at least one numeric value.")
        if not any(char in special_characters for char in value):
            raise ValidationError("Password must contain at least one of the '_-#' following Characters.")
        return value
