''' Define urls.py for the directory users '''
# from django.conf.urls import url   #cor 05/02/2024
from django.urls import path as url
from django.contrib.auth.views import LoginView
#from django.contrib.auth.views import login

from . import views

urlpatterns = [ 
    # login  page 
   # url(r'^login$', LoginView.as_view,{'template_name': 'users/login.html'},name = 'login'),
   url('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
]

