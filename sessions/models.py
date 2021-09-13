from django.db import models
from django.utils.crypto import get_random_string

# Create your models here.
from django_extensions.db.models import TimeStampedModel


class Session(TimeStampedModel):
    session_key = models.TextField(default=get_random_string(8), max_length=8, editable=False)

    def __str__(self):
        return self.session_key


class SessionNote(TimeStampedModel):
    session = models.ForeignKey(Session, related_name='sessions', on_delete=models.CASCADE)
    uuid = models.UUIDField()
    value = models.FloatField(default=0)

    def __str__(self):
        return '%s : %s' % (self.uuid, self.value)
