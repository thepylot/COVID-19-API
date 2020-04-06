from rest_framework import serializers
from core.models import Coronavirus

class CoronavirusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coronavirus
        fields = '__all__'