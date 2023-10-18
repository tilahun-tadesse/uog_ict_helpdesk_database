from rest_framework import serializers
from .models import expert_in
from expert.models import expert_information
from expert.serializers import expertSerializer


class expert_in_serializer(serializers.ModelSerializer):
    expert = expertSerializer

    class Meta:
        model = expert_in
        fields = ['id', 'expert_id', 'expert_in']
