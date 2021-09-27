from django.utils.crypto import get_random_string

from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from rest_framework.fields import SerializerMethodField

from courses.models import Course, Note


class NoteSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    coeff = serializers.FloatField()
    denominator = serializers.IntegerField()
    weight = serializers.FloatField()

    class Meta:
        model = Note
        fields = ('id', 'name', 'coeff', 'denominator', 'weight', 'notes')

    def get_fields(self):
        fields = super(NoteSerializer, self).get_fields()
        fields['notes'] = NoteSerializer(many=True)
        return fields


class CourseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    ects = serializers.FloatField()
    prof = serializers.CharField()
    color = serializers.CharField()

    notes = NoteSerializer(many=True, source='courses')

    class Meta:
        model = Course
        fields = ('id', 'name', 'ects', 'prof', 'color', 'notes')
