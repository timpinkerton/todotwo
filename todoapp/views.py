from django.shortcuts import render
from django.http import HttpResponse

from .models import Todo

# Create your views here.

# this is the index function called in urlpatterns in the todoapp/urls.py
def index(request):
    todoapp = Todo.objects.all()[:10]
    context = {
        'todoapp': 'todoapp'
    }
    return render(request, 'index.html', context) 