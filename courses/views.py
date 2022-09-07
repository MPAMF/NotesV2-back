# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle

from courses.models import Localisation, LocalisationImage, Degree
from courses.serializers import DataSerializer


class DegreeViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    throttle_classes = [AnonRateThrottle]

    def list(self, request, *args, **kwargs):
        data = {'degrees': Degree.objects.all(),
                'localisations': Localisation.objects.all(),
                'localisation_images': LocalisationImage.objects.all()
                }
        serializer = DataSerializer(data)
        return Response(serializer.data)
