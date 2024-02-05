""" From learning_log/learning_logs """
from django.shortcuts import render  
from django.shortcuts import get_object_or_404
from .models import Topic , Entry  # Import the Topic model 
#from .models import Entry  # Import the Entry model
from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse 
from django.urls import reverse
from .forms import TopicForm, EntryForm
# Create your views here.

def index(request):
    """ the home page from learning_log """
    return render(request, 'learning_logs/index.html')


def topics(request):
    """show all topics"""
    topics = Topic.objects.order_by('date_added')  # Use a different variable name
    # context = {'topics': topics}
    # will have to use also the entries  Modif 05/02/2024
    entries = Entry.objects.all()
    return render(request, 'learning_logs/topics.html', {'topics': topics, 'entries': entries})

# ------test to see the entry----    
def test(request):
    entries = Entry.objects.all()
    topics = Topic.objects.all()
    return render(request, 'learning_logs/topics.html', {'entries': entries, 'topics': topics})
# --------end test -------------------------


"""Show a single topic with its entries."""    
from django.http import Http404
def topic(request, topic_id):
 try: 
    topic = get_object_or_404(Topic, id=topic_id)
    entries = topic.entry_set.order_by('date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
 except Topic.DoesNotExist:
        # Raise a custom Http404 exception
    raise Http404("Topic does not exist")


def new_topic(request):
    """ Add a new Topic""" 
    if request.method != 'POST' :
          # no data submitted ;create a blank form.
          form = TopicForm()
    else:  
        # post data submitted ,process data
        form = TopicForm(data=request.POST)
        if form.is_valid():
           form.save()
           return HttpResponseRedirect(reverse('learning_logs:topics')) 


    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


    
#++++++++ end New proposal when we want to add a new entrey and the topic_id does not exist yet ex:http://127.0.0.1:8000/new_entry/25/
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from .models import Topic, Entry
from .forms import EntryForm ,TopicForm # Import your EntryForm & TopicForm

def new_entry(request, topic_id):
    """Add a new entry for a particular topic"""
    topic = get_object_or_404(Topic, id=topic_id)

    if request.method == 'POST':
        form = EntryForm(request.POST)  # Use request.POST to bind POST data to the form
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    else:
        form = EntryForm()  # Create an empty form if it's a GET request

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        #initial request ; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        #POST data submitted; process data
        form = EntryForm(instance=entry, data=request.POST) 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic' , args=[topic.id])) 
    context = {'entry': entry, 'topic': topic, 'form' : form} 
    return render(request, 'learning_logs/edit_entry.html', context)     

def show_entry(request ):
    """ show all the entry"""
    try:
       entries = Entry.objects.all()
       context = {'entries': entries}
       return render(request, 'learning_logs/show_entry.html', context)

    except EntryForm.DoesNotExist:
        # Raise a custom Http404 exception
     raise Http404("Entry does not exist")   