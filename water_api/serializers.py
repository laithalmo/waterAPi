from rest_framework import serializers
from .models import Daily


class WaterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Daily
        fields =['id','numberofcups','numberofsleeping']
