from ctypes.wintypes import HINSTANCE
from django.shortcuts import render
from numpy import character
from requests import Response, request
from rest_framework import generics
from .serializers import on_work_expert_serializer
from .models import on_work_expert
import django_filters.rest_framework
from rest_framework import filters
from django_filters import rest_framework as django_filters
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class on_work_expert_list(generics.ListCreateAPIView):
    queryset = on_work_expert.objects.all()
    serializer_class = on_work_expert_serializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'expert_id', 'campus', 'work_area', 'expert_in','today_on_work','on_work']


class on_work_expert_update(generics.RetrieveUpdateDestroyAPIView):
    queryset = on_work_expert.objects.all()
    serializer_class = on_work_expert_serializer
    lookup_field = 'expert_id'
class on_work_expert_update_one(generics.RetrieveUpdateDestroyAPIView):
    queryset = on_work_expert.objects.all()
    serializer_class = on_work_expert_serializer
    lookup_field = 'expert_id'
