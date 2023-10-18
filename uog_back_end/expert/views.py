from ctypes.wintypes import HINSTANCE
from django.shortcuts import render
from numpy import character
from requests import Response, request
from rest_framework import generics
from .serializers import expertSerializer
from .models import expert_information
from expert_in.models import expert_in
from expert_in.serializers import expert_in_serializer
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class expert_list(generics.ListCreateAPIView):
    queryset = expert_information.objects.all()
    serializer_class = expertSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', "expert_in", "phonenumber"]


# class CustomAPIView(generics.ListAPIView):
#     def get(self, request, *args, **kwargs):
#         date = request.query_params.get('id', None)
#         if date:
#             table1_data = expert_information.objects.filter(id=id)
#             table2_data = expert_in.objects.filter(id=id)
#         else:
#             table1_data = expert_information.objects.all()
#             table2_data = expert_in.objects.all()
#         table1_serializer = expertSerializer(table1_data, many=True)
#         table2_serializer = expert_in_serializer(table2_data, many=True)
#         data = {
#             'table1': table1_serializer.data,
#             'table2': table2_serializer.data,
#         }
#         return Response(data)


class expert_update(generics.RetrieveUpdateDestroyAPIView):
    queryset = expert_information.objects.all()
    serializer_class = expertSerializer
    lookup_field = 'id'


