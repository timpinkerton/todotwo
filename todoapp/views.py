from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# this is the index function called in urlpatterns in the todoapp/urls.py
def index(request):
    return HttpResponse("Hello World")