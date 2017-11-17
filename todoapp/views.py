from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Todo

# Create your views here.

# this is the index function called in urlpatterns in the todoapp/urls.py
def index(request):
            # This allows use of the objects in the Todo class from models.py
    todoapp = Todo.objects.all()[:100]
    
    context = {
        # 'todoapp' is the name used in the for loop in index.html
        'todoapp': todoapp
    }
    return render(request, 'index.html', context) 

# Details View
def details(request, id):
            # This will get a Todo object using the id
    todo = Todo.objects.get(id=id)

    context = {
        'todo': todo
    }
    return render(request, 'details.html', context) 

# Edit View
def edit(request, id):
    # This will test if this is a POST request
    if(request.method == "POST"):
        todo = Todo.objects.get(id=id)

        title = request.POST['title']
        text = request.POST['text']
        # This will replace the title and text with the new info
        todo.title = title
        todo.text = text

        todo.save()
        return redirect('/todoapp')
    else:
        # This is the same as the detail page.          
                # This will get a Todo object using the id
                # and render in the edit page

        todo = Todo.objects.get(id=id)
        context = {
            'todo': todo
        }
        return render(request, 'edit.html', context)  

# Add View
def add(request):
    # This will test if this is a POST request
    # When the submit button in add.html is clicked, it creates a POST request

    if(request.method == "POST"):
        # This gets title and text from the form and puts them in the variables title and text
        title = request.POST["title"]
        text = request.POST["text"]

        todo = Todo(title=title, text=text)
        todo.save()

        return redirect('/todoapp')
    else: 
        return render(request, 'add.html') 
    
# Delete View
def delete(request, id):
    if(request.method == "POST"):
        todo = Todo.objects.get(id=id)

        todo.delete()
        return redirect('/todoapp')
    else:
        todo = Todo.objects.get(id=id)
        context = {
            'todo': todo
        }
        return render(request, 'delete.html', context) 