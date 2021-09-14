import uuid

from django.db import models
from django.utils.crypto import get_random_string

# Create your models here.
from django_extensions.db.models import TimeStampedModel

from courses.models import Note


def generate_random_string():
    return get_random_string(8).upper()


class Session(TimeStampedModel):
    session_key = models.TextField(default=generate_random_string, max_length=8, editable=False, unique=True)

    def __str__(self):
        return self.session_key


class SessionNote(TimeStampedModel):
    session = models.ForeignKey(Session, related_name='sessions', on_delete=models.CASCADE)
    note = models.ForeignKey(Note, related_name='courses', on_delete=models.CASCADE)
    value = models.FloatField(default=0)
    activated = models.BooleanField(default=True)

    def __str__(self):
        return '%s : %s' % (self.note.id, self.value)
