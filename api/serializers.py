from rest_framework import serializers
from api.models import Company
#Creating Seralizers 
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model:Company
        fields="__all__"
        


