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

class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)      
        if not serializer.is_valid():
            return Response({'status':403,'error':serializer.errors,'message':'something went wrong'})
        serializer.save()
        user = User.objects.get(username = serializer.data['username'])
        refresh = RefreshToken.for_user(user)
        return Response({'status':200,'payload':serializer.data,'refresh': str(refresh),
        'access': str(refresh.access_token)})

class LoginUser(APIView):
    def post(self, request):
        #user_obj = User.objects.get(username = request.data['username'])
        user_validate = authenticate(username=request.data['username'], password=request.data['password'])
        if user_validate is not None:
            user = User.objects.get(username = request.data['username'])
            refresh = RefreshToken.for_user(user)
            return Response({'status':200,'refresh': str(refresh),'access': str(refresh.access_token)})
        else:
            return Response({'status':403,'payload':'login not successful'})
#---------------------------------------------------------------------------
