from django.shortcuts import render, redirect
from . models import Todo


def create_todo_view(request):
  todo = request.POST['text']
  Todo.objects.create(body=todo) # create a record in database
  return redirect('/')

def delete_todo_view(request, id):
  todo = Todo.objects.get(id=id)
  todo.delete()
  return redirect('/')

def home_view(request):
  todos = Todo.objects.all()
  context = {
    'todos': todos
  }
  return render(request, 'index.html', context)