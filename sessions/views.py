from rest_framework import viewsets, status, generics, mixins, filters
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound, PermissionDenied, ParseError, ValidationError

from rest_framework.response import Response

from .serializers import SessionSerializer
from .models import Session


class SessionViewSet(mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = SessionSerializer
    queryset = Session.objects

    def create(self, request, *args, **kwargs):
        serializer_context = {
            'request': request
        }

        serializer_data = request.data

        serializer = self.serializer_class(
            data=serializer_data, context=serializer_context
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
