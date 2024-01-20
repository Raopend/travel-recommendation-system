from rest_framework import serializers
from .models import User


class UserInfoSerializer(serializers.ModelSerializer):
    """Serializer for user info."""
    class Meta:
        model = User
        fields = ['id', 'pid', 'username', 'avatar']
