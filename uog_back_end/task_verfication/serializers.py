from rest_framework import serializers
from .models import task_verfication
from customer.serializers import customerSerializer
from customer_ask_help.serializers import customer_ask_help_serializer

class task_verfication_Serializer(serializers.ModelSerializer):
    customer_id = customerSerializer()
    task_id=customer_ask_help_serializer()
    class Meta:
        model = task_verfication
        fields = '__all__'

class task_verfication_Serializer2(serializers.ModelSerializer):

    class Meta:
        model = task_verfication
        fields = '__all__'
