from django.shortcuts import render

import django_filters
from rest_framework import viewsets,filters

from .models import PPMData, NowPPM
from .serializer import PPMDataSerializer, NowPPMSerializer
from rest_framework import permissions

class PPMDataViewSet(viewsets.ModelViewSet):
    queryset = PPMData.objects.all()
    serializer_class = PPMDataSerializer
    permission_classes = (permissions.IsAuthenticated,)

class NowPPMViewSet(viewsets.ModelViewSet):
    queryset = NowPPM.objects.all()
    serializer_class = NowPPMSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)