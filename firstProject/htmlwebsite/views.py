from urllib import request
from django.shortcuts import render
from django.http import  HttpResponse
from musicbeat.models import Song
from .models import SignupForm
def index(request):
     song=Song.objects.all()
     return render(request,'index.html',{'song':song})
def login1(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def home(request):
    song=Song.objects.all()
    return render(request ,'home.html',{'song':song})
def search(request):
    return render(request,'search.html')
def libabry(request):
    song=Song.objects.all()
    return render(request,'libabry.html',{'song':song})
def songs(request):
    song=Song.objects.all()
    return render(request,'songs.html',{'song':song})
def songpost(request,id):
    song=Song.objects.filter(song_id=id).first()
    return render(request,'songpost.html',{'song':song})




