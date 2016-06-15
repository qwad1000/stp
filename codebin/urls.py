from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.snippet_list, name='snippet_list'),
    url(r'^post/(?P<pk>\d+)/$', views.snippet_view, name='snippet_view')
]
