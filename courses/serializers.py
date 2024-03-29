from rest_framework import serializers

from courses.models import Course, Note, Degree, Semester, ExamDate, Localisation, LocalisationImage


class ExamDateSerializer(serializers.ModelSerializer):
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()
    localisation = serializers.IntegerField(source='localisation.id', allow_null=True)
    note = serializers.CharField(source='note.id')

    class Meta:
        model = ExamDate
        fields = ('start', 'end', 'localisation', 'note')


class NoteSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    coeff = serializers.FloatField()
    denominator = serializers.IntegerField()
    weight = serializers.FloatField()
    exam_dates = ExamDateSerializer(many=True, source='date_notes')

    class Meta:
        model = Note
        fields = ('id', 'name', 'coeff', 'denominator', 'weight', 'exam_dates', 'notes')

    def get_fields(self):
        fields = super(NoteSerializer, self).get_fields()
        fields['notes'] = NoteSerializer(many=True)
        return fields


class CourseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    acronym = serializers.CharField()
    ects = serializers.FloatField()
    prof = serializers.CharField()
    weight = serializers.FloatField()
    color = serializers.CharField()
    dark_color = serializers.CharField()
    optional = serializers.BooleanField()

    notes = NoteSerializer(many=True, source='courses')

    class Meta:
        model = Course
        fields = ('id', 'name', 'acronym', 'ects', 'prof', 'weight', 'color', 'dark_color', 'optional', 'notes')


class SemesterSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    number = serializers.IntegerField()
    courses = CourseSerializer(many=True, source='course_semesters')
    exam_dates = serializers.SerializerMethodField()

    class Meta:
        model = Semester
        fields = ('id', 'number', 'courses', 'exam_dates')

    def get_exam_dates(self, obj):
        if not hasattr(obj, 'id') or obj.id is None:
            return []
        result = []
        exam_dates = ExamDate.objects.filter(note__course__semester=obj.id)
        for exam_date in exam_dates:
            result.append(ExamDateSerializer(exam_date).data)
        return result


class DegreeSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    acronym = serializers.CharField()
    semesters = SemesterSerializer(many=True, source='semester_degree')

    class Meta:
        model = Degree
        fields = ('name', 'acronym', 'semesters')

class LocalisationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    x = serializers.FloatField()
    y = serializers.FloatField()
    image = serializers.IntegerField(source='image.id')

    class Meta:
        model = Localisation
        fields = ('id', 'name', 'x', 'y', 'image')


class LocalisationImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    path = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = LocalisationImage
        fields = ('id', 'path', 'description')


class DataSerializer(serializers.Serializer):
    localisations = LocalisationSerializer(many=True)
    localisation_images = LocalisationImageSerializer(many=True)
    degrees = DegreeSerializer(many=True)
