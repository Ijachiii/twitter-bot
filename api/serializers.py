from rest_framework import serializers
from twitterbot.models import TwitterAccountsCheck
from django.contrib.auth import get_user_model


# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
# 
#     class Meta:
#         model = get_user_model()
#         fields = ("username", "email", "password")
# 
#     def create(self, validated_data):
#         user = get_user_model().objects.create_user(**validated_data)
#         return user


class AccountCheckedSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwitterAccountsCheck
        fields ="__all__"