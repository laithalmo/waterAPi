from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_205_RESET_CONTENT
)
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from .models import Daily
from .serializers import WaterSerializer
# Create your views here.

class WaterList(ListCreateAPIView):
    queryset = Daily.objects.all()
    serializer_class = WaterSerializer

class WaterDetails(RetrieveUpdateDestroyAPIView):
    queryset = Daily.objects.all()
    serializer_class = WaterSerializer

def save_water_sleep(request):
    if len(request.body) <= 0:
        return Response({'error': 'unknown'}, status=400)
    
    data = JSONParser().parse(request)
    water = data["water"]
    sleep = data["sleep"]
    