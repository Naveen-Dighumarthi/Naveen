from django.contrib import admin
from django.urls import  path,include
from database import views


urlpatterns = [
    path('', views.home,name='dbpage'),
]