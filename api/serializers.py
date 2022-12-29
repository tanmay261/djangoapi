from rest_framework import serializers
from api.models import Company,Employee
#Creating Seralizers 
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    # Generally id is hidden so we expose it and make it a READ ONLY Column
    company_id=serializers.ReadOnlyField()
    # Meta generally means data about some data
    class Meta:
        model=Company
        fields="__all__"

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    # Generally id is hidden so we expose it and make it a READ ONLY Column
    id=serializers.ReadOnlyField()
    # Meta generally means data about some data
    class Meta:
        model=Employee
        fields="__all__"
        


