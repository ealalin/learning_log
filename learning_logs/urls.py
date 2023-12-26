''' Define urls.py for the directory learning_logs '''
''' -----------------------corection from the 26/12/2023 ----------------
from django.urls import re_path
from . import views

urlpatterns = [ 
    # home page 
    re_path(r'^$', views.index, name='index'),
]
----------------------end -corection from the 26/12/2023 ----------------
'''

# from django.conf.urls import url   #cor 26/12/2023
from django.urls import re_path as url2
from . import views

urlpatterns = [ 
    # home page 
    url2('^$', views.index, name='index'),
               
]

