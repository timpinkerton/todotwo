from django.contrib import admin

# Register your models here.

# To see the Todo section in the django admin.
from .models import Todo

admin.site.register(Todo)