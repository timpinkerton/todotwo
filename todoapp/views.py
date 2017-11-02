from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Todo

# Create your views here.

# this is the index function called in urlpatterns in the todoapp/urls.py
def index(request):
            # This allows use of the objects in the Todo class from models.py
    todoapp = Todo.objects.all()[:10]
    
    context = {
        # 'todoapp' is the name used in the for loop in index.html
        'todoapp': todoapp
    }
    return render(request, 'index.html', context) 

def details(request, id):
            # This will get a Todo object using the id
    todo = Todo.objects.get(id=id)

    context = {
        'todo': todo
    }
    return render(request, 'details.html', context) 

def edit(request, id):
            # This will get a Todo object using the id
    todo = Todo.objects.get(id=id)

    context = {
        'todo': todo
    }
    return render(request, 'edit.html', context) 

def add(request):
    # This will test if this is a POST request
    if(request.method == "POST"):
        title = request.POST["title"]
        text = request.POST["text"]

        todo = Todo(title=title, text=text)
        todo.save()

        return redirect('/todoapp')
    else: 
        return render(request, 'add.html')