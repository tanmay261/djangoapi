from django.contrib import admin
from django.urls import path,include
from api.views import CompanyViewSet
from rest_framework import routers

router=routers.DefaultRouter()

# Here R'' means a raw string
router.register(r'companies',CompanyViewSet)
urlpatterns = [

    path('',include(router.urls))
]
