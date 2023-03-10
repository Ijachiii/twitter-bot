from rest_framework import serializers
from twitterbot.models import TwitterAccountsCheck
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.response import Response
from rest_framework import status


class AccountCheckedSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwitterAccountsCheck
        fields ="__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "username", "email",)

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = ["username","email",]

#     def create(self, validated_data):
#         user = get_user_model().objects.create_user(**validated_data)
#         return user


# class RegisterSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(
#         required=True,
#         validators=[UniqueValidator(queryset=get_user_model().objects.all())]
#     )
#     password = serializers.CharField(
#         write_only=True, 
#         required=True, 
#         validators=[validate_password])
#     password2 = serializers.CharField(write_only=True, required=True)

#     class Meta:
#         model = get_user_model()
#         fields = ("username", 'email','password', 'password2',)

#     def validate(self, attrs):
#         if attrs['password'] != attrs['password2']:
#             raise serializers.ValidationError(
#                 {"password": "Password fields didn't match."})
#         return attrs
  
#     def create(self, validated_data):
#         user = get_user_model().objects.create(
#         username=validated_data["username"],
#         email=validated_data['email'],
#         )

#         user.set_password(validated_data['password'])
#         user.save()
#         return user


