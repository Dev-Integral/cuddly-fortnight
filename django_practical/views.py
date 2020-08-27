from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    """The homepage for django practical."""
    return render(request, 'django_practical/index.html')

def topics(request):
    """The topics page for django practical."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}    
    return render(request, 'django_practical/topics.html', context)

def topic(request, topic_id):
    """The topic details page for django practical."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = { 'topic': topic, 'entries': entries}
    return render(request, 'django_practical/topic.html', context)