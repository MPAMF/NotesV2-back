from rest_framework import serializers

from courses.models import Course, Note, TpGroup, TdGroup, Semester, ExamDate


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
    weight = serializers.FloatField()
    color = serializers.CharField()
    dark_color = serializers.CharField()

    notes = NoteSerializer(many=True, source='courses')

    class Meta:
        model = Course
        fields = ('id', 'name', 'ects', 'prof', 'weight', 'color', 'dark_color', 'notes')


class ExamDateSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField()
    note = serializers.CharField(source='note.id')

    class Meta:
        model = ExamDate
        fields = ('date', 'note')


class TpGroupSerializer(serializers.ModelSerializer):
    number = serializers.IntegerField()
    exam_dates = ExamDateSerializer(many=True, source='tp_groups')

    class Meta:
        model = TpGroup
        fields = ('number', 'exam_dates')


class TdGroupSerializer(serializers.ModelSerializer):
    number = serializers.IntegerField()
    tp_groups = TpGroupSerializer(many=True, source='td_groups')

    class Meta:
        model = TdGroup
        fields = ('number', 'tp_groups')


class SemesterSerializer(serializers.ModelSerializer):
    number = serializers.IntegerField()
    activated = serializers.BooleanField()
    courses = CourseSerializer(many=True, source='course_semesters')
    td_groups = TdGroupSerializer(many=True, source='semesters')

    class Meta:
        model = Semester
        fields = ('number', 'activated', 'courses', 'td_groups')
