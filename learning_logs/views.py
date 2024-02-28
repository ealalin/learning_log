""" From learning_log/learning_logs """
from django.shortcuts import render  
from django.shortcuts import get_object_or_404
from .models import Topic , Entry  # Import the Topic model 
from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse 
from django.urls import reverse
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.models import User 
from django.http import Http404


# Create your views here.

def index(request):
    """ the home page from learning_log """
    return render(request, 'learning_logs/index.html')

@login_required

def topics(request):
    """show all topics"""
   # topics = Topic.objects.order_by('date_added')  # Use a different variable name
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    # context = {'topics': topics}
    # will have to use also the entries  Modif 05/02/2024
    entries = Entry.objects.all()
    return render(request, 'learning_logs/topics.html', {'topics': topics, 'entries': entries})

# ------test to see the entry----    
def test(request):
    entries = Entry.objects.all()
    topics = Topic.objects.all()
    user = User.objects.get(username='ealalin2')
    print("*****user_id :",user.id ,"******")

    return render(request, 'learning_logs/topics.html', {'entries': entries, 'topics': topics})
# --------end test -------------------------


"""Show a single topic with its entries."""    

def topic(request, topic_id):
 try: 
    topic = get_object_or_404(Topic, id=topic_id)
    #Make sure that the topic belong to the current user
    check_topic_owner(topic.owner , request.user )
    entries = topic.entry_set.order_by('date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
 except Topic.DoesNotExist:
        #Raise a custom Http404 exception
    raise Http404("Topic does not exist")
 
 
def edit_topic(request, topic_id):
  """Edit an existing topic"""
  topic = Topic.objects.get(id=topic_id)
  #Make sure that the topic belong to the current user
  check_topic_owner(topic.owner,request.user)
  try: 
    if request.method != 'POST':
        #initial request ; pre-fill form with the current topic.
        form = TopicForm(instance=topic)
    else:
        #POST data submitted; process data
        form = TopicForm(instance=topic, data=request.POST) 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic' , args=[topic.id])) 
    context = {'topic': topic, 'topic': topic, 'form' : form} 
    return render(request, 'learning_logs/edit_topic.html', context)     
  except Topic.DoesNotExist:
         #Raise a custom Http404 exception
    raise Http404("Topic does not exist")

@login_required
def new_topic(request):
    """Take the information of the user"""
    user = User.objects.get(username=request.user)
    """ Add a new Topic""" 
    if request.method != 'POST' :
       # no data submitted ;create a blank form.
       form = TopicForm()
    else:  
        # post data submitted ,process data
        print("post data submitted ,process data")    #print for info
        form = TopicForm(data=request.POST)
        if form.is_valid():
            # Set the owner of the topic to the current user. #cor13/02/2024
            print("Set the owner of the topic to the current user. #cor13/02/2024")  #print for info
            new_topic = form.save(commit=False)
            new_topic.owner_id = user.id  # Assuming request.user is the current authenticated user.
            new_topic.owner_name=request.user
            new_topic.save()
            # form.save()
        return HttpResponseRedirect(reverse('learning_logs:topics')) 


    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

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

@login_required

def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    #Make sure that the topic belong to the current user
    check_topic_owner(topic.owner,request.user)
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


def show_edit_entry(request ):
    """ show all the entry"""
    try:
       entries = Entry.objects.all()
       context = {'entries': entries}
       return render(request, 'learning_logs/show_edit_entry.html', context)
    except EntryForm.DoesNotExist:
        # Raise a custom Http404 exception
     raise Http404("Entry does not exist") 

    
def check_topic_owner(topic_owner , request_user ):
    """ make sure that the logged user use his own topic , if not quit the page"""
    if (topic_owner !=  request_user):
       print("topic_owner :",topic_owner ,"is not the request_user :",request_user, " we quit this page.")
       raise Http404
       


           




