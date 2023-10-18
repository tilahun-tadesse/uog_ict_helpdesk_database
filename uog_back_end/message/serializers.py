from rest_framework import serializers
# import customer
from .models import message
from user.serializers import userSerializer
from user.models import user_information


class message_serializer(serializers.ModelSerializer):
    # customer = customerSerializer()
    user_id = userSerializer()
    class Meta:
        model = message
        fields = '__all__'


class message_serializer2(serializers.ModelSerializer):

    class Meta:
        model = message
        fields = '__all__'
   