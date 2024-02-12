''' Define urls.py for the directory users '''
# from django.conf.urls import url   #cor 05/02/2024
from django.urls import path as url
#from django.contrib.auth.views import login ,logout
from django.contrib.auth.views import LoginView , LogoutView

from . import views

urlpatterns = [ 
    # login  page 
   # url(r'^login$', LoginView.as_view,{'template_name': 'users/login.html'},name = 'login'),
   # login page
   url('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
   # logout page 
   url('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
   # registratie pagina
   url('register/', views.register, name= 'register' ),
  

]

