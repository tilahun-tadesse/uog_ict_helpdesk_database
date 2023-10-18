from django.shortcuts import render
from rest_framework import generics
from .serializers import completed_task_Serializer
from .models import completed_task
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class completed_task_list(generics.ListCreateAPIView):
    queryset = completed_task.objects.all()
    serializer_class = completed_task_Serializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date']


class completed_task_update(generics.RetrieveUpdateDestroyAPIView):
    queryset = completed_task.objects.all()
    serializer_class = completed_task_Serializer
