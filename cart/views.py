from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import authenticate, login
# Create your views here.

class CartAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        Cart_objs = Cart.objects.filter(username = self.request.query_params.get('username'))
        serializer = CartSerializer(Cart_objs,many=True)
        return Response({'status':200,'message':serializer.data})

    def post(self, request):
        data = request.data
        serializer = CartSerializer(data = request.data)
        if not serializer.is_valid():
            return Response({'status':403,'error':serializer.errors,'message':'something went wrong'})
        serializer.save()
        return Response({'status':200,'payload':serializer.data})

    def put(self, request):
        try:
            Cart_obj = Cart.objects.get(username = request.data['username'])
            serializer = CartSerializer(Cart_obj,data = request.data)
            if not serializer.is_valid():
                return Response({'status':403,'error':serializer.errors,'message':'something went wrong'})
            serializer.save()
            return Response({'status':200,'payload':serializer.data})
        except Exception as e:
            return Response({'status':403,'message':'invalid id'})

    def patch(self, request):
        try:
            Cart_obj = Cart.objects.get(username = request.data['username'])
            serializer = CartSerializer(Cart_obj,data = request.data,partial = True)
            if not serializer.is_valid():
                return Response({'status':403,'error':serializer.errors,'message':'something went wrong'})
            serializer.save()
            return Response({'status':200,'payload':serializer.data})
        except Exception as e:
            return Response({'status':403,'message':'invalid id'})

    def delete(self, request):
        try:
            Cart_obj = Cart.objects.get(username = request.data['username'],product_id = request.data['product_id'])
            Cart_obj.delete()
            return Response({'status':200, 'message':'deleted'})
        except Exception as e:
            return Response({'status':403,'message':'invalid id'})
