from django.conf.urls import url
# imports the views.py from the current folder
from . import views 

urlpatterns = [
    # $ means to start with and end with
    # this is the root of the todoapp
    # it looks for a function in the views file called index
    url(r'^$', views.index, name='index'),

]