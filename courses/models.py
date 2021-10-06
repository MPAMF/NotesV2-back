import uuid

from django.db import models
# Create your models here.
from django_extensions.db.models import TimeStampedModel


class Semester(TimeStampedModel):
    number = models.IntegerField(default=0)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return 'Semester %s' % self.number


class TdGroup(TimeStampedModel):
    number = models.IntegerField(default=0)
    semester = models.ForeignKey(Semester, related_name='semesters', on_delete=models.CASCADE)

    def __str__(self):
        return '%s TD %s' % (str(self.semester), self.number)


class TpGroup(TimeStampedModel):
    number = models.IntegerField(default=0)
    td_group = models.ForeignKey(TdGroup, related_name='td_groups', on_delete=models.CASCADE)

    def __str__(self):
        return '%s TP %s' % (str(self.td_group), self.number)


class Course(TimeStampedModel):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=64)
    ects = models.FloatField()
    prof = models.CharField(max_length=64)
    weight = models.FloatField(default=0)
    color = models.CharField(max_length=7)
    optional = models.BooleanField(default=False)
    dark_color = models.CharField(max_length=7, default='#7417D5')
    semester = models.ForeignKey(Semester, related_name='course_semesters', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Note(TimeStampedModel):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=64)
    coeff = models.FloatField()
    denominator = models.IntegerField(default=20)
    weight = models.FloatField(default=0)
    course = models.ForeignKey(Course, related_name='courses', on_delete=models.CASCADE, default=None, blank=True,
                               null=True)
    note = models.ForeignKey('self', related_name='notes', default=None,
                             blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        course = self.course if self.course is not None else self.note.course
        return self.name + ' (' + str(course) + ')'


class ExamDate(TimeStampedModel):
    date = models.DateTimeField()
    note = models.ForeignKey(Note, related_name='date_notes', on_delete=models.CASCADE)
    tp_group = models.ForeignKey(TpGroup, related_name='tp_groups', on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (str(self.note), str(self.tp_group))
