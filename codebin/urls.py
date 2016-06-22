from django.conf.urls import url
import base58

from . import views

urlpatterns = [
    url(r'^(?:(my)/)?$', views.snippet_list, name='snippet_list'),
    url(r'^search/', views.search, name='search'),
    url(r'^snippet/new/$', views.snippet_new, name='snippet_new'),
    url(r'^snippet/(?P<base58>[{0}]+)/$'.format(base58.alphabet), views.snippet_view, name='snippet_view'),
    url(r'^snippet/edit/(?P<base58>[{0}]+)/$'.format(base58.alphabet), views.snippet_edit, name='snippet_edit'),
]
