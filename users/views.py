from django.shortcuts import render
# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    """ logout the user out"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    """register a new user"""
    if request.method != 'POST':
        #display a blanc form
        form = UserCreationForm()
    else:
        # proceed with the creation of the form
        form = UserCreationForm(data= request.POST)  
        if form.is_valid(): 
           new_user = form.save()     
           # log the user in and redirect to home page
           authenticated_user = authenticate(username=new_user.username, 
            password=request.POST['password1'])
           login(request, authenticated_user)
        return HttpResponseRedirect(reverse('learning_logs:index'))
       

           
    context = {'form': form }        
    return render(request, 'users/register.html' , context)          
          