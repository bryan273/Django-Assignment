from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

class TodoListEntry(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_finished = models.BooleanField(default=False, null=True, blank=True)