from django.shortcuts import render
from .models import Todo
from django.http import HttpResponse

# Create your views here.
def todos_list(request):
    all_todos = Todo.objects.all()

    return render(request, 'todos/index.html', {'todos' : all_todos})
    
def todos_detail(request, todo_id):
    todo1 = Todo.objects.get(id=todo_id)
    
    return render(request, 'todos/detail.html', {'todo' : todo1})
    
def tag_list(request, tag):
    tag_todos = Todo.objects.filter(tag__name__iexact=tag)
    
    return render(request, 'todos/taglist.html', {'todos' : tag_todos, 'tag' : tag})