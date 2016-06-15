from django.conf.urls import url
from base58 import alphabet

from . import views

urlpatterns = [
    url(r'^$', views.snippet_list, name='snippet_list'),
    url(r'^snippet/(?P<base58>[{0}]+)/$'.format(alphabet), views.snippet_view, name='snippet_view')
]
