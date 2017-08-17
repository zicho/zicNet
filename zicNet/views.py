from django.shortcuts import render
from django.http import HttpResponse
from feed.models import Feed_entry
from forms import Feed_entryForm
from datetime import datetime


def index(request):
 
    return render(request, 'index.html')
    
def feed(request):
 
    entries = Feed_entry.objects.all().order_by('-publish_date')
 
    if request.method == 'POST':
    
        form = Feed_entryForm(request.POST)
        
        if form.is_valid():
            
            cd = form.cleaned_data
            entry = Feed_entry.objects.create(body=cd['body'])
            form = Feed_entryForm()
        
    else:
    
        form = Feed_entryForm()
    
    return render(request, 'feed.html', {'entries' : entries, 'form' : form })

def profile(request):
 
    return render(request, 'profile.html')

def search(request):
    
    errors = []

    if 'q' in request.GET:
        q = request.GET['q']
   
        if not q:

            errors.append("Please enter a search query!")

        elif len(q) > 20:
            
            errors.append("Search query can be max <strong>20</strong> chars.")             

        else:
            entries = Feed_entry.objects.filter(body__icontains=q)
            return render(request, 'search.html', {'entries' : entries, 'query' : q})   
 
    return render(request, 'search.html', {'errors' : errors})
