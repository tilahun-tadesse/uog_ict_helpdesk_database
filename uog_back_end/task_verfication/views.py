from ctypes.wintypes import HINSTANCE
from django.shortcuts import render
from numpy import character
from requests import Response, request
from rest_framework import generics
from .serializers import task_verfication_Serializer,task_verfication_Serializer2
from .models import task_verfication
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
# Create your views here.


class task_varfication_list(generics.ListCreateAPIView):
    queryset = task_verfication.objects.all()
    serializer_class = task_verfication_Serializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','expert_id','customer_id','expert_verify','user_verify']

# class task_varfication_list_or(generics.ListCreateAPIView):
#     serializer_class = task_verfication_Serializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['id','expert_id','customer_id','expert_verify','user_verify']
#     def get_queryset(self):
#         queryset = task_verfication.objects.all()
#         expert_verify = self.request.query_params.get('expert_verify')
#         user_verify = self.request.query_params.get('user_verify')
#         if expert_verify == 'NO' or user_verify == 'NO':
#             queryset = queryset.filter(Q(expert_verify='NO') | Q(user_verify='NO'))
#         return queryset
class task_varfication_list1(generics.ListCreateAPIView):
    queryset = task_verfication.objects.all()
    serializer_class = task_verfication_Serializer2    
class task_varfication_update(generics.RetrieveUpdateDestroyAPIView):
    queryset = task_verfication.objects.all()
    serializer_class = task_verfication_Serializer
class task_verfication_update_one(generics.RetrieveUpdateDestroyAPIView):
    queryset = task_verfication.objects.all()
    serializer_class = task_verfication_Serializer
    lookup_field = 'task_id'
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
