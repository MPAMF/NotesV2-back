from django.shortcuts import render


# Create your views here.
class CourseViewSet(mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = SessionSerializer
    queryset = Session.objects
