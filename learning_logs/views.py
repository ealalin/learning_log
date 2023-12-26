""" From learning_log/learning_logs """
from django.shortcuts import render

# Create your views here.

def index(request):
    """ the home page from learning_log """
    return render(request, 'learning_logs/index.html')