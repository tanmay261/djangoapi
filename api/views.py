from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
#LEARN
#Function to get all employees of a company using /companies/{id}/employees
    

    #LEARN
    # Here pk is the Primary Key of the 'company' class 
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        try:
            #LEARN
            # Get a company using the primary key
            company=Company.objects.get(pk=pk)

            #LEARN
            # Get Employees using the foreign key 'company'
            emps=Employee.objects.filter(company=company)

            emps_serialiser =EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(emps_serialiser.data)
        except Exception as e:
            print(e)
            return Response(
                {
                    'message':"Error ! Company might not exist"
                }
            )


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
