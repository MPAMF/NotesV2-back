import uuid

from django.db import models

# Create your models here.
from django_extensions.db.models import TimeStampedModel


class Course(TimeStampedModel):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=64)
    ects = models.FloatField()
    prof = models.CharField(max_length=64)
    color = models.CharField(max_length=7)

    def __str__(self):
        return self.name


class Note(TimeStampedModel):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=64)
    coeff = models.FloatField()
    course = models.ForeignKey(Course, related_name='courses', on_delete=models.CASCADE, default=None, blank=True,
                               null=True)
    note = models.ForeignKey('self', related_name='notes', default=None,
                             blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
