from rest_framework import serializers
from .models import on_work_expert


class on_work_expert_serializer(serializers.ModelSerializer):

    class Meta:
        model = on_work_expert
        fields = '__all__'
