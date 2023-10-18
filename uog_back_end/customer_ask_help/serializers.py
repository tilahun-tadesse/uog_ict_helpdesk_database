from rest_framework import serializers
# import customer
from .models import customer_ask_help



class customer_ask_help_serializer(serializers.ModelSerializer):
 
    class Meta:
        model = customer_ask_help
        fields = '__all__'

    # def create(self, validated_data):
    #     customer_data = validated_data.pop('customer')
    #     # Create the nested objects separately
    #     customer_info = customer_information.objects.create(**customer_data)
    #     # Create the Pharmacy object and associate the nested objects
    #     pharmacy = customer_ask_help.objects.create(
    #         document=customer_info, **validated_data)
    #     return pharmacy
