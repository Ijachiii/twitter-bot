from rest_framework import serializers
from twitterbot.models import TwitterAccountChecked

class AccountCheckedSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwitterAccountChecked
        fields ="__all__"