from django.contrib import admin
from django.urls import path
from htmlwebsite import views

urlpatterns = [
    path('',views.index,name="index"),
    path('home/',views.home,name="home"),
     path('login/',views.login1,name="login"),
     path('signup/',views.signup,name='signup'),
    path('search/',views.search,name="search"),
     path('libabry/',views.libabry,name="libabry"),
     path('songs/',views.songs,name="songs"),
     path('songs/<int:id>',views.songpost,name="songpost"),
    
    

]    
