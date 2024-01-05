''' Define urls.py for the directory learning_logs '''
# from django.conf.urls import url   #cor 26/12/2023
from django.urls import re_path as url
from . import views

urlpatterns = [ 
    # home page 
    url('^$', views.index, name='index'),

    # show all topics
    url(r'^topics/$', views.topics, name='topics'),
    # detail page for a single topic
    url(r'^topics/(?P<topic_id>\d+)/$' , views.Topic , name='topic'),      
]

