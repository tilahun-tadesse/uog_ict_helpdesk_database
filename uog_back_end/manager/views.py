from ctypes.wintypes import HINSTANCE
from django.shortcuts import render
from numpy import character
from requests import Response, request
from rest_framework import generics
from .serializers import mangerSerializer
from .models import manager_information

import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class manager_list(generics.ListCreateAPIView):
    queryset = manager_information.objects.all()
    serializer_class = mangerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', "phonenumber"]



class manager_update(generics.RetrieveUpdateDestroyAPIView):
    queryset = manager_information.objects.all()
    serializer_class = mangerSerializer
    lookup_field = 'id'


