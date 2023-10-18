from rest_framework import generics
from .serializers import expert_in_serializer
from .models import expert_in
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class expert_in_list(generics.ListCreateAPIView):
    queryset = expert_in.objects.all()
    serializer_class = expert_in_serializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'expert_id', 'expert_in']


class expert_in_update(generics.RetrieveUpdateDestroyAPIView):
    queryset = expert_in.objects.all()
    serializer_class = expert_in_serializer
    lookup_field = 'expert_id'
