from rest_framework import serializers

from .models import Session, SessionNote, SessionSelectedCourse


class SessionSelectedCourseSerializer(serializers.ModelSerializer):
    course = serializers.UUIDField(format='hex_verbose', source='course.id')
    activated = serializers.BooleanField()

    class Meta:
        model = SessionSelectedCourse
        fields = ('course', 'activated')

    def create(self, validated_data):
        selected_course = SessionSelectedCourse.objects.create(**validated_data)
        return selected_course


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
    selected_courses = SessionSelectedCourseSerializer(many=True, required=False)

    class Meta:
        model = Session
        fields = ('session_key', 'notes', 'selected_courses')

    def create(self, validated_data):
        session = Session.objects.create()
        return session

    def update(self, instance, validated_data):
        notes = validated_data.pop('notes')

        for note in notes:
            SessionNote.objects.update_or_create(
                session_id=self.context['session_id'],
                note_id=note['note']['id'],
                defaults={
                    'value': note['value'],
                    'activated': note['activated']
                }
            )

        selected_courses = [] if 'selected_courses' in validated_data else validated_data.pop('selected_courses')

        for selected_course in selected_courses:
            SessionSelectedCourse.objects.update_or_create(
                session_id=self.context['session_id'],
                note_id=selected_course['note']['id'],
                defaults={
                    'activated': selected_course['activated']
                }
            )

        return instance
