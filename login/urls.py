from django.urls import path, include
from django.contrib import admin
from .views import *
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
  #  path('',views.home, name='home'),
  #  path('student',views.post_student),
  #  path('update-student/<id>/',views.update_student),
  #  path('delete-student/<id>/',views.delete_student),

  path('register/',RegisterUser.as_view()),
  path('login/',LoginUser.as_view()),

  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]