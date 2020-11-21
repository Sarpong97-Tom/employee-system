
from django.core import exceptions
from rest_framework.exceptions import ParseError

from rest_framework import serializers
from .models import User, UserProfile
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework_jwt.settings import api_settings
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile

        fields = ('first_name', 'last_name')


class UserRegistrationSerializer(serializers.ModelSerializer):

    profile = UserSerializer(required=False)
    first_name = serializers.CharField(write_only=True,required=True)
    last_name = serializers.CharField(write_only=True,required=True)
    password = serializers.CharField(write_only=True,required=True)
    password_confirm = serializers.CharField(write_only=True,required=True)


    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
        

    def create(self, validated_data):
        if validated_data['password'] != validated_data['password_confirm']:
            raise ValueError("Passwords must match")
        else:
            user = User.objects.create_user(email = validated_data['email'],password=validated_data['password'])
            UserProfile.objects.create(
                user=user,
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
        
            )
    
        return user

class SuperUSerRegistrationSerializer(serializers.ModelSerializer):

    profile = UserSerializer(required=False)
    first_name = serializers.CharField(write_only=True,required=True)
    last_name = serializers.CharField(write_only=True,required=True)
    password = serializers.CharField(write_only=True,required=True)
    password_confirm = serializers.CharField(write_only=True,required=True)


    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
        

    def create(self, validated_data):
        if validated_data['password'] != validated_data['password_confirm']:
            raise ValueError("Passwords must match")
        else:
            user = User.objects.create_superuser(email = validated_data['email'],password=validated_data['password'])
            UserProfile.objects.create(
                user=user,
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
        
            )
    
        return user
            






JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

class UserLoginSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'email':user.email,
            'token': jwt_token
        }