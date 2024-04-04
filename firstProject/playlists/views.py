from django.shortcuts import render
from django.http import HttpResponse, HttpResponse


def home(request):
    return HttpResponse("<h1>This is Playlists</h1>")

