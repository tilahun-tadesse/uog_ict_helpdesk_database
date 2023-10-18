from ctypes.wintypes import HINSTANCE
from django.shortcuts import render
from requests import Response, request
from rest_framework import generics
from .serializers import userSerializer
from .models import user_information
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class user_list(generics.ListCreateAPIView):
    queryset = user_information.objects.all()
    serializer_class = userSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_name', 'password','phonenumber','roll','email']
class user_update(generics.RetrieveUpdateDestroyAPIView):
    queryset = user_information.objects.all()
    serializer_class = userSerializer
    lookup_field = 'phonenumber'
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
