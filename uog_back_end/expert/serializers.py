from rest_framework import serializers
from .models import expert_information
from expert_in.models import expert_in


class expertSerializer(serializers.ModelSerializer):

    class Meta:
        model = expert_information
        fields = '__all__'

# class CustomSerializer(serializers.ModelSerializer):
#     expert_in = serializers.CharField(source='name')
#     table1_description = serializers.CharField(source='description')
#     table2_id = serializers.IntegerField(source='table2.id')
#     table2_address = serializers.CharField(source='table2.address')
#     table2_city = serializers.CharField(source='table2.city')

#     class Meta:
#         model = Table1
#         fields = ('id', 'table1_name', 'table1_description', 'table2_id', 'table2_address', 'table2_city')
