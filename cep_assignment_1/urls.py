from django.conf.urls import patterns, include, url
from django.contrib import admin
from todos import views
from django.views.generic import ListView, DetailView
from todos.models import Todo

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cep_assignment_1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^todos/', ListView.as_view(model=Todo, template_name="todos/index.html"), name='todo_list'),
    url(r'^todo/(?P<pk>\d+)$', views.TodoDetail.as_view(template_name="todos/detail.html"), name='todos_detail'),
    #url(r'^todo/(?P<todo_id>\d+)$', views.todos_detail, name = "todos_detail"),
    #url(r'^tagged/(?P<tag>.*)$', views.tag_list, name='tag_list'),
    url(r'^tagged/(?P<tag>.*)$', views.TagList.as_view(template_name="todos/taglist.html"), name = "tag_list"),
    url(r'^add/$', views.TodoCreate.as_view(), name='todo_add'),
    url(r'^todo/(?P<pk>\d+)/edit/$', views.TodoUpdate.as_view(),  name='todo_update'),
    url(r'^todo/(?P<pk>\d+)/delete/$', views.TodoDelete.as_view(template_name="todos/delete.html"), name='todo_delete'),
)