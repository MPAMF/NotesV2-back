from django.utils.crypto import get_random_string

from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from rest_framework.fields import SerializerMethodField

from .models import Session


class SessionSerializer(serializers.ModelSerializer):
    session_key = serializers.CharField(min_length=8, max_length=8, read_only=True)

    class Meta:
        model = Session
        fields = ('id', 'session_key')

    def create(self, validated_data):
        session = Session.objects.create(**validated_data)
        return session
