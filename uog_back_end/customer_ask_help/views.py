from ctypes.wintypes import HINSTANCE
from django.shortcuts import render
from numpy import character
from requests import Response, request
from rest_framework import generics
from .serializers import customer_ask_help_serializer
from .models import customer_ask_help
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class customer_ask_help_list(generics.ListCreateAPIView):
    queryset = customer_ask_help.objects.all()
    serializer_class = customer_ask_help_serializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['expert_id','task_id']

class customer_ask_help_update(generics.RetrieveUpdateDestroyAPIView):
    queryset = customer_ask_help.objects.all()
    serializer_class = customer_ask_help_serializer

    # def partial_update(self, request, *args, **kwargs):
    #     response_with_updated_instance = super(
    #         expertSerializer, self).partial_update(request, *args, **kwargs)
    #     expertSerializer.objects.my_func(request.user, self.get_object())
    #     return response_with_updated_instance

# class expert_update_one(generics.RetrieveUpdateAPIView):
#     def patch(self, request, pk, amount):
#         # if no model exists by this PK, raise a 404 error
#         model = get_object_or_404(MyModel, pk=pk)
#         # this is the only field we want to update
#         data = {"amount": model.amount + int(amount)}
#         serializer = MyModelSerializer(model, data=data, partial=True)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         # return a meaningful error response
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
