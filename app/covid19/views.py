from rest_framework import viewsets, mixins

from core.models import Coronavirus
from covid19 import serializers

class CovidViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Coronavirus.objects.all()
    serializer_class = serializers.CoronavirusSerializer
