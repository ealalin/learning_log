""" From learning_log/learning_logs """
from django.shortcuts import render  
from django.shortcuts import get_object_or_404
from .models import Topic  # Import the Topic model
# Create your views here.

def index(request):
    """ the home page from learning_log """
    return render(request, 'learning_logs/index.html')

#def topics(request):
#    """show alle topic"""
#    topics = topics.objects.order_by('date_added')   #date_added
#    context = {'topics':topics}
#    return render(request, 'learning_logs/topics.html', context)
def topics(request):
    """show all topics"""
    topics_list = Topic.objects.order_by('date_added')  # Use a different variable name
    context = {'topics': topics_list}
    return render(request, 'learning_logs/topics.html', context)
    
#-----------------------------------------------
# def topics(request):
#      """Show all topics."""
#      topics = Topic.objects.all()
#      context = {'topics': topics}
#      return render(request, 'learning_logs/topics.html', context)

#def topic(request, topic_id):
    """Show a single topic with its entries."""
    topic = get_object_or_404(Topic, id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)



