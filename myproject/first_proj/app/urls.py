from django.conf.urls import patterns, url

from . import views 

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^make_json', views.make_json, name ='make_json'),
    url(r'^graph', views.graph),
]
