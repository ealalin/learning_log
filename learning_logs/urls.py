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
    url(r'^topic/(?P<topic_id>\d+)/$' , views.topic , name='topic'),  
    # page for additing a new topic
    url(r'^new_topic/$' , views.new_topic , name='new_topic'), 
    # new_entry    
    url(r'^new_entry/(?P<topic_id>\d+)/$' , views.new_entry , name='new_entry'), 
     # test    
     url(r'^test/$', views.test, name='test'),    
]

