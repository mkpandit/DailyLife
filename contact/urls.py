from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

#app_name = 'contact'

#mapping the urls for this app
urlpatterns = [
    url(r'^index.html$', views.index, name='contact_home'),
    url(r'^$', views.index, name='contact_index'),
    url(r'^addcontact/$', views.addContact, name='add_contact'),
    url(r'^details/(?P<pk>\d+)/$', views.contactDetail, name='contact_details'),
    url(r'^edit/(?P<pk>\d+)/$', views.editContact, name='edit_contact'),
]