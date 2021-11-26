from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *


# Create your views here.

class BrandAPI(APIView):
    #authentication_classes = [JWTAuthentication]
    #permission_classes = [IsAuthenticated]
    def get(self, request):
        Brand_objs = Brand.objects.all()
        serializer = BrandSerializer(Brand_objs,many=True)
        return Response({'status':200,'message':serializer.data})

    def post(self, request):
        data = request.data
        serializer = BrandSerializer(data = request.data)
        if not serializer.is_valid():
            return Response({'status':403,'error':serializer.errors,'message':'something went wrong'})
        serializer.save()
        return Response({'status':200,'payload':serializer.data})

    def put(self, request):
        try:
            Brand_obj = Brand.objects.get(company_name = request.data['company_name'])
            serializer = BrandSerializer(Brand_obj,data = request.data)
            if not serializer.is_valid():
                return Response({'status':403,'error':serializer.errors,'message':'something went wrong'})
            serializer.save()
            return Response({'status':200,'payload':serializer.data})
        except Exception as e:
            return Response({'status':403,'message':'invalid id'})

    def patch(self, request):
        try:
            Brand_obj = Brand.objects.get(company_name = request.data['company_name'])
            serializer = BrandSerializer(Brand_obj,data = request.data,partial = True)
            if not serializer.is_valid():
                return Response({'status':403,'error':serializer.errors,'message':'something went wrong'})
            serializer.save()
            return Response({'status':200,'payload':serializer.data})
        except Exception as e:
            return Response({'status':403,'message':'invalid id'})

    def delete(self, request):
        try:
            Brand_obj = Brand.objects.get(company_name = request.data['company_name'])
            Brand_obj.delete()
            return Response({'status':200, 'message':'deleted'})
        except Exception as e:
            return Response({'status':403,'message':'invalid id'})




class Product_CategoryAPI(APIView):
    #authentication_classes = [JWTAuthentication]
    #permission_classes = [IsAuthenticated]
    def get(self, request):
        Product_Category_objs = Product_Category.objects.all()
        serializer = ProductCategorySerializer(Product_Category_objs,many=True)
        return Response({'status':200,'message':serializer.data})

    def post(self, request):
        data = request.data
        serializer = ProductCategorySerializer(data = request.data)
        if not serializer.is_valid():
            return Response({'status':403,'error':serializer.errors,'message':'something went wrong'})
        serializer.save()
        return Response({'status':200,'payload':serializer.data})

    def put(self, request):
        try:
            Product_Category_obj = Product_Category.objects.get(category_name = request.data['category_name'])
            serializer = ProductCategorySerializer(Product_Category_obj,data = request.data)
            if not serializer.is_valid():
                return Response({'status':403,'error':serializer.errors,'message':'something went wrong'})
            serializer.save()
            return Response({'status':200,'payload':serializer.data})
        except Exception as e:
            return Response({'status':403,'message':'invalid id'})

    def patch(self, request):
        try:
            Product_Category_obj = Product_Category.objects.get(category_name = request.data['category_name'])
            serializer = ProductCategorySerializer(Product_Category_obj,data = request.data,partial = True)
            if not serializer.is_valid():
                return Response({'status':403,'error':serializer.errors,'message':'something went wrong'})
            serializer.save()
            return Response({'status':200,'payload':serializer.data})
        except Exception as e:
            return Response({'status':403,'message':'invalid id'})

    def delete(self, request):
        try:
            Product_Category_obj = Product_Category.objects.get(category_name = request.data['category_name'])
            Product_Category_obj.delete()
            return Response({'status':200, 'message':'deleted'})
        except Exception as e:
            return Response({'status':403,'message':'invalid id'})

@api_view(['GET'])
def ProductSort(request,orderby):
    Products_objs = Products.objects.order_by(orderby)
    serializer = ProductsSerializer(Products_objs,many=True)
    return Response({'status':200,'message':serializer.data})

@api_view(['GET'])
def ProductSearch(request,search):
    Products_objs = Products.objects.filter(product_name = search)
    serializer = ProductsSerializer(Products_objs,many=True)
    return Response({'status':200,'message':serializer.data})



class ProductsAPI(APIView):
    #authentication_classes = [JWTAuthentication]
    #permission_classes = [IsAuthenticated]
    def get(self, request):
        Products_objs = Products.objects.all()
        serializer = ProductsSerializer(Products_objs,many=True)
        return Response({'status':200,'message':serializer.data})

    def post(self, request):
        data = request.data
        serializer = ProductsSerializer(data = request.data)
        if not serializer.is_valid():
            return Response({'status':403,'error':serializer.errors,'message':'something went wrong'})
        serializer.save()
        return Response({'status':200,'payload':serializer.data})

    def put(self, request):
        try:
            Products_obj = Products.objects.get(Products_id = request.data['Products_id'])
            serializer = ProductsSerializer(Products_obj,data = request.data)
            if not serializer.is_valid():
                return Response({'status':403,'error':serializer.errors,'message':'something went wrong'})
            serializer.save()
            return Response({'status':200,'payload':serializer.data})
        except Exception as e:
            return Response({'status':403,'message':'invalid id'})

    def patch(self, request):
        try:
            Products_obj = Products.objects.get(Products_id = request.data['Products_id'])
            serializer = ProductsSerializer(Products_obj,data = request.data,partial = True)
            if not serializer.is_valid():
                return Response({'status':403,'error':serializer.errors,'message':'something went wrong'})
            serializer.save()
            return Response({'status':200,'payload':serializer.data})
        except Exception as e:
            return Response({'status':403,'message':'invalid id'})

    def delete(self, request):
        try:
            Products_obj = Products.objects.get(Products_id = request.data['Products_id'])
            Products_obj.delete()
            return Response({'status':200, 'message':'deleted'})
        except Exception as e:
            return Response({'status':403,'message':'invalid id'})

#-----------------------------------------------------------------------------------------------------------------------