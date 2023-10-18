from rest_framework import serializers
from .models import manager_information
class mangerSerializer(serializers.ModelSerializer):

    class Meta:
        model = manager_information
        fields = '__all__'
