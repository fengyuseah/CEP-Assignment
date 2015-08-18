from django.shortcuts import render, redirect
from .models import Todo
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from todos.forms import TodoForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accounts.models import UserProfile

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

class TodoList(ListView):
    model = Todo
    
    queryset = Todo.objects.all()
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TodoList, self).dispatch(*args, **kwargs)
    
    def get_queryset(self):
        currentuser = UserProfile.objects.get(user=self.request.user)
        self.queryset = Todo.objects.filter(user=currentuser)
        return self.queryset

    def get_context_data(self, **kwargs):
        context = super(TodoList, self).get_context_data(**kwargs)
        context['currentuser'] = UserProfile.objects.get(user=self.request.user)
        return context

class TagList(ListView):
    model = Todo
    
    queryset = Todo.objects.all()
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TagList, self).dispatch(*args, **kwargs)
    
    #@method_decorator(login_required)
    def get_queryset(self):
        currentuser = UserProfile.objects.get(user=self.request.user)
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
        todos = Todo.objects.filter(user=currentuser).filter(query).distinct().order_by('tag__name')
        self.queryset = todos #Setting the queryset to allow get_context_data to apply count
        return todos
    
    #@method_decorator(login_required)
    def get_context_data(self, **kwargs):
        context = super(TagList, self).get_context_data(**kwargs)
        context['tag'] = self.kwargs['tag']
        context['currentuser'] = UserProfile.objects.get(user=self.request.user)
        return context
        
class TodoCreate(TemplateView):
    model = Todo
    todo_form_class = TodoForm
    template_name = 'todos/todo_form.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TodoCreate, self).dispatch(*args, **kwargs)
        
    def get(self, request, *args, **kwargs):
        kwargs.setdefault("form", self.todo_form_class())
        kwargs.setdefault('currentuser', UserProfile.objects.get(user=self.request.user))
        return super(TodoCreate, self).get(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        form_args = {
            'data': self.request.POST,
        }
        #form = self.todo_form_class(**form_args)
        form = self.todo_form_class(request.POST)
        curruser = UserProfile.objects.get(user=self.request.user)
        obj = form.save(commit=False)
        obj.user = curruser #Save the note note under that user
        obj.save() #save the new object
        return redirect('/todos/')
        #return super(TodoCreate, self).get(request)
    
class TodoUpdate(UpdateView):
    model = Todo
    form_class = TodoForm

class TodoDetail(DetailView):
    model = Todo
    
class TodoDelete(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_list')

class Landing(TemplateView):
    template_name = "todos/landing.html"
