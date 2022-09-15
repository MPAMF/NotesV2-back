import uuid

from django.db import models
# Create your models here.
from django.utils.timezone import now
from django_extensions.db.models import TimeStampedModel


class Degree(models.Model):
    name = models.CharField(max_length=64)
    acronym = models.CharField(max_length=16, default="")

    def __str__(self):
        return self.name


class Semester(TimeStampedModel):
    number = models.IntegerField(default=0)
    degree = models.ForeignKey(Degree, related_name='semester_degree',
                               on_delete=models.CASCADE, null=True,
                               default=None)

    def __str__(self):
        return 'Semester %s' % self.number


class Course(TimeStampedModel):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=64)
    acronym = models.CharField(max_length=16, default="")
    ects = models.FloatField()
    prof = models.CharField(max_length=64)
    weight = models.FloatField(default=0)
    color = models.CharField(max_length=7)
    optional = models.BooleanField(default=False)
    dark_color = models.CharField(max_length=7, default='#7417D5')
    semester = models.ForeignKey(Semester, related_name='course_semesters',
                                 on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Note(TimeStampedModel):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=64)
    coeff = models.FloatField()
    denominator = models.IntegerField(default=20)
    weight = models.FloatField(default=0)
    course = models.ForeignKey(Course, related_name='courses',
                               on_delete=models.CASCADE, default=None,
                               blank=True,
                               null=True)
    note = models.ForeignKey('self', related_name='notes', default=None,
                             blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        course = self.course if self.course is not None else self.note.course
        return self.name + ' (' + str(course) + ')'


class LocalisationImage(models.Model):
    path = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return '%s' % self.path


class Localisation(models.Model):
    name = models.CharField(max_length=64)
    x = models.FloatField(default=0)
    y = models.FloatField(default=0)
    image = models.ForeignKey(LocalisationImage,
                              related_name='localisation_images', null=True,
                              on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.name


class ExamDate(TimeStampedModel):
    start = models.DateTimeField(default=now)
    end = models.DateTimeField(default=now)
    localisation = models.ForeignKey(Localisation,
                                     related_name='date_localisations',
                                     on_delete=models.CASCADE,
                                     null=True)
    note = models.ForeignKey(Note, related_name='date_notes',
                             on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % str(self.note)
