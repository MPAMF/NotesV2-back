from rest_framework import serializers

from .models import Session, SessionNote


class SessionNoteSerializer(serializers.ModelSerializer):
    note = serializers.UUIDField(format='hex_verbose', source='note.id')
    value = serializers.FloatField()
    activated = serializers.BooleanField()

    class Meta:
        model = SessionNote
        fields = ('note', 'value', 'activated')

    def create(self, validated_data):
        session_note = SessionNote.objects.create(**validated_data)
        return session_note

    def validate_note(self, value):
        return value.id if hasattr(value, 'id') else value


class SessionSerializer(serializers.ModelSerializer):
    session_key = serializers.CharField(min_length=8, max_length=8, read_only=True)
    notes = SessionNoteSerializer(many=True)

    class Meta:
        model = Session
        fields = ('session_key', 'notes')

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
