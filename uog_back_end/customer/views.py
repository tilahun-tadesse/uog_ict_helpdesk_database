from django.shortcuts import render
from rest_framework import generics
from .serializers import customerSerializer
from .models import customer_information
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class customer_list(generics.ListCreateAPIView):
    queryset = customer_information.objects.all()
    serializer_class = customerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['phonenumber', 'firstName', "lastName", 'customer_id']
class customer_update(generics.RetrieveUpdateDestroyAPIView):
    queryset = customer_information.objects.all()
    serializer_class = customerSerializer
    lookup_field = 'phonenumber'
