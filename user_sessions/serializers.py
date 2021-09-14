from django.utils.crypto import get_random_string

from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from rest_framework.fields import SerializerMethodField

from .models import Session, SessionNote


class SessionNoteSerializer(serializers.ModelSerializer):
    note = serializers.UUIDField()
    value = serializers.FloatField()

    class Meta:
        model = SessionNote
        fields = ('uuid', 'note')

    def create(self, validated_data):
        session_note = SessionNote.objects.create(**validated_data)
        return session_note


class SessionSerializer(serializers.ModelSerializer):
    session_key = serializers.CharField(min_length=8, max_length=8, read_only=True)
    notes = SessionNoteSerializer(many=True)

    class Meta:
        model = Session
        fields = ('id', 'session_key', 'notes')

    def create(self, validated_data):
        session = Session.objects.create(**validated_data)
        return session
