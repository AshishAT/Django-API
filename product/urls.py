from django.urls import path, include
from django.contrib import admin
from .views import *
from rest_framework.authtoken import views
urlpatterns = [
    path('brand/',BrandAPI.as_view()),
  path('category/',Product_CategoryAPI.as_view()),
  path('products/',ProductsAPI.as_view()),
  path('products/sort/<orderby>',ProductSort),
  path('products/search/<search>',ProductSearch),
]