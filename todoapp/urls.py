from django.conf.urls import url
# imports the views.py from the current folder
from . import views 

urlpatterns = [
    # ^ means to start with and $ means end with
    # this is the root of the todoapp
    # it looks for a function in the views file called index
    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<id>\w{0,50})/$', views.details),
    url(r'^add', views.add, name='add'),
    url(r'^edit/(?P<id>\w{0,50})/$', views.edit, name='edit'),
    url(r'^delete/(?P<id>\w{0,50})/$', views.delete, name='delete')
]