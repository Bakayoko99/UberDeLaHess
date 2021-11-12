from django.db import models
from rest_framework import serializers
from .models import PriceEstimate, TimeEstimate

class PriceEstimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceEstimate
        fields=('id','start_latitude','start_longitude','end_latitude','end_longitude')

class TimeEstimateSerializer(serializers.ModelSerializer):
    class Beta:
        model = TimeEstimate
        fields = ('id','start_latitude','start_longitude')