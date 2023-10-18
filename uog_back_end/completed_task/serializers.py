from rest_framework import serializers
from .models import completed_task


class completed_task_Serializer(serializers.ModelSerializer):

    class Meta:
        model = completed_task
        fields = '__all__'
