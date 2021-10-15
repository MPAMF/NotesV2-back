# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle

from courses.models import Semester, Localisation, LocalisationImage, ExamDate
from courses.serializers import DataSerializer


class SemesterViewSet(mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    throttle_classes = [AnonRateThrottle]

    def list(self, request, *args, **kwargs):
        data = {'semesters': Semester.objects.all(),
                'localisations': Localisation.objects.all(),
                'localisation_images': LocalisationImage.objects.all()
                }
        serializer = DataSerializer(data)
        return Response(serializer.data)
