from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from myapp.models import Product
from myapp.serializers import ProductSerializer


# Create your views here.

#CLASS BASED VIEW
class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#localhost:8000/api/products/27
#DELETE, PUT/PATCH, GET

class ProductDetailAPIView(APIView):
    def get(self, request, id):
        product = get_object_or_404(Product, id=id)#it has an id because we are targeting specific product
        serializer = ProductSerializer(product)#serializer is a translator from object to json or vice versa
        return Response(serializer.data)

    def put(self, request, id):
        product = get_object_or_404(Product, id=id)
        serializer = ProductSerializer(product, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        product = get_object_or_404(Product, id=id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#TODO: api that can delete many products ie id[7, 80, 65] --mass delete
#TODO: fetching by category eg when you click skin care all products in that category are fetched
#explore api django rest framework tutorial using APIView/viewSets
#Research model relationships in django
#Auth in django res framework

#200-ok, 201-saved success, 400-bad data, 401,403 -permissions, 500-error on server,404-NotFound