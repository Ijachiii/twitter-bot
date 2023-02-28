from rest_framework import serializers
from twitterbot.models import TwitterAccountsCheck

class AccountCheckedSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwitterAccountsCheck
        fields ="__all__"