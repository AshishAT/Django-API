from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'