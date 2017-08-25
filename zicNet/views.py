from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from feed.models import Feed_entry, Comment
from forms import Feed_entryForm, Feed_commentForm
from datetime import datetime



def login_user(request):
    
    if request.method == 'POST':
        username = request.POST['username']   
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/login/')
   
    return render(request, 'login.html')

@login_required(login_url='/login/')
def logout_user(request):
    
    logout(request)
    return HttpResponseRedirect('/login/')

@login_required(login_url='/login/')	
def index(request):
    
    try:
 	
        entry =  Feed_entry.objects.latest('publish_date')
        return render(request, 'index.html', {'entry' : entry})     
  
    except:
   
	    return render(request, 'index.html')

@login_required(login_url='/login/')	
def feed(request):
 
    entries = Feed_entry.objects.all().order_by('-publish_date')
    cmt_form = Feed_commentForm()
    
    if request.method == 'POST':
    
        form = Feed_entryForm(request.POST)
        
        if form.is_valid():
            
            cd = form.cleaned_data
            Feed_entry.objects.create(body=cd['body'], author=request.user)
            form = Feed_entryForm()
        
    else:
    
        form = Feed_entryForm()
    
    return render(request, 'feed.html', {'entries' : entries, 'form' : form, 'cmt_form' : cmt_form })


def quick_comment_feed(request, id):
    
    entry = Feed_entry.objects.get(id=id)

    if request.method == 'POST':
 
        form = Feed_commentForm(request.POST)
        
        if form.is_valid():
            
            cd = form.cleaned_data
            Comment.objects.create(body=cd['body'], belongs_to=entry, author=request.user)
            form = Feed_commentForm()
        
    else:
    
        form = Feed_commentForm()
    
    return HttpResponseRedirect('/feed/')

@login_required(login_url='/login/')    
def comment_feed(request, id):
    
    entry = Feed_entry.objects.get(id=id)
    comments = Comment.objects.all().filter(belongs_to=id)
    
    if request.method == 'POST':
    
        form = Feed_commentForm(request.POST)
        
        if form.is_valid():
            
            cd = form.cleaned_data
            Comment.objects.create(body=cd['body'], belongs_to=entry, author=request.user)
            form = Feed_commentForm()
        
    else:
    
        form = Feed_commentForm()
    
    return render(request, 'feed_comment.html', {'entry' : entry, 'comments' : comments, 'form' : form})
	
@login_required(login_url='/login/')
def profile(request):
 
    return render(request, 'profile.html')

@login_required(login_url='/login/')
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
