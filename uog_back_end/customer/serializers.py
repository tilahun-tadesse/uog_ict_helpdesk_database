from rest_framework import serializers
from .models import customer_information


class customerSerializer(serializers.ModelSerializer):

    class Meta:
        model = customer_information
        fields = '__all__'
