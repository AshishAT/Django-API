from django.urls import path, include
from django.contrib import admin
from .views import *
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
path('cart',CartAPI.as_view()),
]
