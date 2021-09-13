# Create your views here.
from rest_framework import mixins, viewsets

from user_sessions.models import Session
from user_sessions.serializers import SessionSerializer


class CourseViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = SessionSerializer
    queryset = Session.objects
