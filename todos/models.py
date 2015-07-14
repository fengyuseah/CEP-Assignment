from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    priority_list = (('!!!', 'HIGH'), ('!!', 'MEDIUM'), ('!', 'LOW'), (' ', '------'))
    
    task = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    priority = models.CharField(max_length=3, choices=priority_list, default=' ')
    due_date = models.DateTimeField(null=True, blank=True)
    tag = models.ManyToManyField('Tag', related_name='todos', null=True, blank=True)
    
    def __str__(self):
        return self.task
        
    def is_due_today(self):
        return self.due_date < timezone.now()
        
class Tag(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name