from django.shortcuts import render
from musicbeat.models import Song

def index(request):
    song=Song.objects.all()
    return render(request,'libabry.html',{'song':song})


# Create your views here.
