from django.conf.urls import patterns, include, url
from django.contrib import admin
from todos import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cep_assignment_1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^todos/', views.todos_list),
    url(r'^todo/(?P<todo_id>\d+)$', views.todos_detail, name = "todos_detail"),
    url(r'^tagged/(?P<tag>.*)$', views.tag_list, name='tag_list'),
)