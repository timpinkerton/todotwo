from django.db import models

# python package datetime to use in created_at
from datetime import datetime

# Creating the Todo Model
class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    
    # This will return the Todo.title from the class above
    def __str__(self):
        return self.title