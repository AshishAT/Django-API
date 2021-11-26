from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Category
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
        brand_name = BrandSerializer()
        category_name =  ProductCategorySerializer()
