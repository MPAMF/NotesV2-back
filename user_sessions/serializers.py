from django.utils.crypto import get_random_string

from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from rest_framework.fields import SerializerMethodField

from .models import Session, SessionNote


class SessionNoteSerializer(serializers.ModelSerializer):
    note = serializers.UUIDField()
    value = serializers.FloatField()
    activated = serializers.BooleanField()

    class Meta:
        model = SessionNote
        fields = ('note', 'value', 'activated')

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
        session = Session.objects.create()
        return session

    def update(self, instance, validated_data):
        notes = validated_data.pop('notes')

        for note in notes:
            SessionNote.objects.update_or_create(
                session_id=self.context['session_id'],
                note_id=note['note'],
                defaults={
                    'value': note['value'],
                    'activated': note['activated']
                }
            )

        return instance


class RequestSessionNotesSerializer(serializers.Serializer):
    notes = SessionNoteSerializer(many=True)
