from rest_framework import serializers
from .models import user_information


class userSerializer(serializers.ModelSerializer):

    class Meta:
        model = user_information
        fields = '__all__'
