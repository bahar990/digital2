from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import Productserializer
from rest_framework.response import Response
from rest_framework import status
from .models import Product

# Create your views here.


class Productlist(APIView):
    def get(self,request):
        products=Product.objects.all()
        serializer=Productserializer(products,many=True)
        return Response(serializer.data)