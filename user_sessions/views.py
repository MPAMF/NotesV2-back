from rest_framework import viewsets, status, mixins
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle

from .models import Session
from .serializers import SessionSerializer


class SessionViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = SessionSerializer
    queryset = Session.objects
    throttle_classes = [AnonRateThrottle]

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

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        try:
            serializer_instance = self.queryset.get(session_key=pk)
        except Session.DoesNotExist:
            raise NotFound('This session does not exist!')

        serializer = SessionSerializer(serializer_instance)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        serializer_context = {'request': request, 'session_key': pk}

        try:
            serializer_instance = self.queryset.get(session_key=pk)
        except Session.DoesNotExist:
            raise NotFound('This session does not exist!')

        serializer_context['session_id'] = serializer_instance.id

        serializer = SessionSerializer(
            serializer_instance,
            context=serializer_context,
            data=request.data
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
