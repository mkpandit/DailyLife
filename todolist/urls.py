from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

#app_name = 'portal'

#mapping the urls for this app
urlpatterns = [
    url(r'^index.html$', views.index, name='home'),
    url(r'^$', views.index, name='index'),
    url(r'^addtodo/$', views.add_todo, name='add_todo'),
    url(r'^details/(?P<pk>\d+)/$', views.to_do_detail, name='todo_details'),
    url(r'^delete/(?P<pk>\d+)/$', views.to_do_delete, name='todo_delete'),
    url(r'^edit/(?P<pk>\d+)/$', views.edit_todo, name='edit_todo'),
    url(r'^search/$', views.search, name='search')
]