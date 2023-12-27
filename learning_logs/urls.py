''' Define urls.py for the directory learning_logs '''
# from django.conf.urls import url   #cor 26/12/2023
from django.urls import re_path as url2
from . import views

urlpatterns = [ 
    # home page 
    url2('^$', views.index, name='index'),
               
]

