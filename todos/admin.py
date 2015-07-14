from django.contrib import admin
from .models import Todo, Tag

class TodoInline(admin.StackedInline): #no TiledInline :(
    model = Todo.tag.through
    extra = 0
    
class TagAdmin(admin.ModelAdmin):
    inlines = [TodoInline,]
    model = Tag

admin.site.register(Todo)
admin.site.register(Tag, TagAdmin)