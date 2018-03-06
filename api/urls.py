#urls.py

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView

#Define urls to access the apis and its actions (POST, PUT, DELETE)
urlpatterns = {
    url(r'^contact/$', CreateView.as_view(), name="create"),
	url(r'^contact/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)