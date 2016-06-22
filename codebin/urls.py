from django.conf.urls import url
from base58 import alphabet

from . import views

urlpatterns = [
    url(r'^(?:(my)/)?$', views.snippet_list, name='snippet_list'),
    url(r'^search/', views.search, name='search'),
    url(r'^snippet/new/$', views.snippet_new, name='snippet_new'),
    url(r'^snippet/(?P<base58>[{0}]+)/$'.format(alphabet), views.snippet_view, name='snippet_view'),
]
