# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.response import Response

from courses.models import Course
from courses.serializers import CourseSerializer
from user_sessions.models import Session
from user_sessions.serializers import SessionSerializer


class CourseViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
