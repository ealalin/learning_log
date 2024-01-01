""" From learning_log/learning_logs """
from django.shortcuts import render
from .models import Topic
# Create your views here.

def index(request):
    """ the home page from learning_log """
    return render(request, 'learning_logs/index.html')

def topics(request):
    """show all topics"""
    topics = Topic.objects.order_by('date_added')   #date_added
    context = {'topics':topics}
    return render(request,'learning_logs/topics.html', context)