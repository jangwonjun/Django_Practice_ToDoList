from django.db import models
from django.contrib.auth.models import User

class TodoItem(models.Model):
    title = models.CharField(max_length=200)  
    description = models.TextField(blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)