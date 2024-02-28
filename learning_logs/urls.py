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
    # page for editind an entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$' , views.edit_entry , name='edit_entry'),
    #  name='show all entry 
     url(r'^show_entry/$', views.show_entry , name='show_entry'),
     # show all the entry + edit
    #  url(r'^show_entri/(?P<entri_id>\d+)$', views.show_entri , name='show_entri'),
    # url(r'^edit_entri/(?P<entri_id>\d+)/$', views.show_entri, name='edit_entri'),


]
