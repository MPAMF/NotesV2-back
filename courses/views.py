# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle

from courses.models import Semester
from courses.serializers import SemesterSerializer


class SemesterViewSet(mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = SemesterSerializer
    queryset = Semester.objects
    throttle_classes = [AnonRateThrottle]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
