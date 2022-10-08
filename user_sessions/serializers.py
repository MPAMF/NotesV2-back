from drf_recaptcha.fields import ReCaptchaV3Field
from rest_framework import serializers

from courses.models import Semester
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
    planning_url = serializers.URLField(required=False)
    notes = SessionNoteSerializer(many=True)
    selected_courses = SessionSelectedCourseSerializer(many=True, required=False)
    semester = serializers.PrimaryKeyRelatedField(queryset=Semester.objects.all(), allow_null=True)
    recaptcha = ReCaptchaV3Field(action="sessions", write_only=True)

    class Meta:
        model = Session
        fields = ('session_key', 'planning_url', 'notes', 'selected_courses', 'semester', 'recaptcha')

    def create(self, validated_data):
        session = Session.objects.create()
        return session

    def update(self, instance, validated_data):
        notes = validated_data.pop('notes') if 'notes' in validated_data else []

        if 'semester' in validated_data:
            instance.semester = validated_data['semester']

        if 'planning_url' in validated_data:
            instance.planning_url = validated_data['planning_url']

        if 'tp_group' in validated_data:
            instance.tp_group = validated_data['tp_group']

        for note in notes:
            SessionNote.objects.update_or_create(
                session_id=self.context['session_id'],
                note_id=note['note']['id'],
                defaults={
                    'value': note['value'],
                    'activated': note['activated']
                }
            )

        selected_courses = validated_data.pop('selected_courses') if 'selected_courses' in validated_data else []

        for selected_course in selected_courses:
            SessionSelectedCourse.objects.update_or_create(
                session_id=self.context['session_id'],
                course_id=selected_course['course']['id'],
                defaults={
                    'activated': selected_course['activated']
                }
            )
        instance.save()
        return instance
