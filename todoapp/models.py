from django.db import models

# python package datetime to use in created_at
from datetime import datetime

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    
    # This will return the title given above
    def __str__(self):
        return self.title