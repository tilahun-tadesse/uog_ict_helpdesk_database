from rest_framework import serializers
from .models import work_area
from expert.serializers import expertSerializer


class work_area_serializer(serializers.ModelSerializer):

    # expertid = expertSerializer(read_only=True)

    class Meta:
        model = work_area
        fields = ('id', 'expertid', 'work_areas', 'expert_in', 'campus')
