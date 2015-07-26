from django.shortcuts import render
from .models import Todo
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from todos.forms import TodoForm
from django.core.urlresolvers import reverse_lazy

# Create your views here.
'''
def todos_list(request):
    all_todos = Todo.objects.all()

    return render(request, 'todos/index.html', {'todos' : all_todos})

def todos_detail(request, todo_id):
    todo1 = Todo.objects.get(id=todo_id)
    
    return render(request, 'todos/detail.html', {'todo' : todo1})

def tag_list(request, tag):
    tag_todos = Todo.objects.filter(tag__name__iexact=tag)
    
    return render(request, 'todos/taglist.html', {'todos' : tag_todos, 'tag' : tag})
'''

class TagList(ListView):
    model = Todo
    
    queryset = Todo.objects.all()
    def get_queryset(self):
        tagn = self.kwargs['tag']
        #pieces = tags.split('/') #extract different tags separated by /
        
        #queries = [Q(tag__name__iexact=value) for value in pieces]
        # Take one Q object from the list
        #query = queries.pop()
        query = Q(tag__name__iexact=tagn)
        # Or the Q object with the ones remaining in the list
        #for item in queries:
        #query |= item
        # Query the model
        todos = Todo.objects.filter(query).distinct().order_by('tag__name')
        self.queryset = todos #Setting the queryset to allow get_context_data to apply count
        return todos
        
    def get_context_data(self, **kwargs):
        context = super(TagList, self).get_context_data(**kwargs)
        context['tag'] = self.kwargs['tag']
        return context
        
class TodoCreate(CreateView):
    model = Todo
    form_class = TodoForm
    
class TodoUpdate(UpdateView):
    model = Todo
    form_class = TodoForm

class TodoDetail(DetailView):
    model = Todo
    
class TodoDelete(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_list')