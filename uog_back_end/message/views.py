# from ctypes.wintypes import HINSTANCE
# from django.shortcuts import render
# from numpy import character
# from requests import Response, request
# from rest_framework import generics
# from .serializers import message_serializer, message_serializer2
# from .models import message
# import django_filters.rest_framework
# from django_filters.rest_framework import DjangoFilterBackend
# from django.db.models import Q
# from django_filters import rest_framework as filters
# Create your views here.
from telnetlib import STATUS
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q
from ctypes.wintypes import HINSTANCE
from django.shortcuts import render
from numpy import character
from requests import Response, request
from rest_framework import generics
from .serializers import message_serializer
from .serializers import message_serializer2
from .models import message
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
# Create your views here.


class message_list(generics.ListCreateAPIView):
    queryset = message.objects.all().order_by('-id')
    serializer_class = message_serializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'from_number', 'to_number', 'message_seen','expert_in','roll']
    def get_queryset(self):
        queryset = super().get_queryset()
        pairs = self.request.GET.getlist('pair')

        if pairs:
            q_object = Q()
            for pair in pairs:
                from_number, to_number = pair.split('|')
                q_object |= (
                    (Q(from_number=from_number) & Q(to_number=to_number)) |
                    (Q(from_number=to_number) & Q(to_number=from_number))
                )

            queryset = queryset.filter(q_object)

        return queryset

class message_list1(generics.ListCreateAPIView):
    queryset = message.objects.all()
    serializer_class = message_serializer2
class message_list2(generics.ListCreateAPIView):
    queryset = message.objects.all().order_by('-id')
    serializer_class = message_serializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'from_number', 'to_number', 'message_seen','expert_in','roll']
    def get_queryset(self):
        queryset = super().get_queryset()
        pairs = self.request.GET.getlist('pair')

        if pairs:
            q_object = Q()
            for pair in pairs:
                from_number, to_number = pair.split('|')
                q_object |= (
                    (Q(from_number=from_number) & Q(to_number=to_number)) |
                    (Q(from_number=to_number) & Q(to_number=from_number))
                )

            queryset = queryset.filter(q_object)
            queryset = queryset.first()
        return queryset

class MessageUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = message.objects.all()
    serializer_class = message_serializer

    def patch(self, request, *args, **kwargs):
        from_number = request.query_params.get('from_number')
        to_number = request.query_params.get('to_number')

        # Filter messages that match the criteria
        messages_to_update = message.objects.filter(
            from_number=from_number,
            to_number=to_number,
            message_seen="No"
        )

        # Loop through all matching messages and update them
        for Message in messages_to_update:
            Message.message_seen = "Yes"
            Message.save()

        # Return a JSON response with a message
        return Response({'message': 'All matching messages updated successfully.'}, status=STATUS.HTTP_200_OK)

    # def get_object(self):
    #     to_number = self.request.query_params.get('to_number')
    #     from_number = self.request.query_params.get('from_number')
    #     message_seen = self.request.query_params.get('message_seen')

    #     try:
    #         obj = message.objects.get(
    #             to_number=to_number,
    #             from_number=from_number,
    #             message_seen=message_seen
    #         )
    #         return obj
    #     except message.DoesNotExist:
    #         return None

    # def partial_update(self, request, *args, **kwargs):
    #     instance = self.get_object()

    #     if instance is None:
    #         return Response({'message': 'Message not found.'}, status=404)
        
    #     new_roll = request.data.get('message_seen')
    #     instance.message_seen = new_roll
    #     instance.save()
        
    #     return Response({'message': 'Roll updated successfully.'})
    # def get_object(self):
    #     # Retrieve the object based on the provided query parameters
    #     to_number = self.request.query_params.get('to_number')
    #     from_number = self.request.query_params.get('from_number')
    #     message_seen = self.request.query_params.get('message_seen')

    #     # Add any additional conditions you want to include in the query
    #     conditions = Q(to_number=to_number,from_number=from_number,message_seen=message_seen)
    #     obj = message.objects.get(conditions)
    #     return obj
class message_delete(generics.RetrieveUpdateDestroyAPIView):
    queryset = message.objects.all()
    serializer_class = message_serializer2