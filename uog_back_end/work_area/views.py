
from rest_framework import generics
from .serializers import work_area_serializer
from .models import work_area
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class user_list(generics.ListCreateAPIView):
    queryset = work_area.objects.all()
    serializer_class = work_area_serializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'expertid', 'work_areas', "expert_in", "campus"]


class user_update(generics.RetrieveUpdateDestroyAPIView):
    queryset = work_area.objects.all()
    serializer_class = work_area_serializer
