from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

from django.core.paginator import Paginator

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

from feed.models import Feed_entry, Comment
from users.models import private_message


from forms import Feed_entryForm, Feed_commentForm, Password_changeForm, send_messageForm
from datetime import datetime

def page_not_found(request):
    return render_to_response('404.html')

def login_user(request):
    
    success = True

    if request.method == 'POST':
    
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
        else:
            login_fail = True
            return render(request, 'login.html', {'login_fail' : login_fail})           
    
    return render(request, 'login.html')        

def account_request(request):
    return render(request, 'account_request.html')
    
@login_required(login_url='/login/')
def password_change(request):

    if request.method == 'POST':
        form = Password_changeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return HttpResponseRedirect('/profile/')

    else:
        form = Password_changeForm(request.user)
    return render(request, 'password_change.html', {'form': form})
    
@login_required(login_url='/login/')
def logout_user(request):
    
    logout(request)
    return HttpResponseRedirect('/login/')

@login_required(login_url='/login/')    
def index(request):
    
    try:
     
        entry =  Feed_entry.objects.latest('publish_date')
        cmt_form = Feed_commentForm()

        return render(request, 'index.html', {'entry' : entry, 'cmt_form' : cmt_form})     
  
    except:
   
        return render(request, 'index.html')

@login_required(login_url='/login/')    
def feed(request):
 
    entries = Feed_entry.objects.all().order_by('-publish_date')
    cmt_form = Feed_commentForm()
    
    success = False
    
    if request.method == 'POST':
    
        form = Feed_entryForm(request.POST)
        
        if form.is_valid():
            
            cd = form.cleaned_data
            Feed_entry.objects.create(body=cd['body'], author=request.user)
            form = Feed_entryForm()
            success = True
        
    else:
    
        form = Feed_entryForm()
    
    return render(request, 'feed.html', {'entries' : entries, 'form' : form, 'cmt_form' : cmt_form, 'success' : success })

def quick_comment_feed(request, id):
    
    entry = Feed_entry.objects.get(id=id)

    cmt_success = False
    
    if request.method == 'POST':
 
        form = Feed_commentForm(request.POST)
        
        if form.is_valid():
            
            cd = form.cleaned_data
            Comment.objects.create(body=cd['body'], belongs_to=entry, author=request.user)
            form = Feed_commentForm()
            cmt_success = True
        
    else:
    
        form = Feed_commentForm()
    
    return HttpResponseRedirect('/feed/', {'cmt_success' : cmt_success})

@login_required(login_url='/login/')    
def comment_feed(request, id):
    
    entry = Feed_entry.objects.get(id=id)
    comments = Comment.objects.all().filter(belongs_to=id)
    success = False
    
    if request.method == 'POST':
    
        form = Feed_commentForm(request.POST)
        
        if form.is_valid():
            
            cd = form.cleaned_data
            Comment.objects.create(body=cd['body'], belongs_to=entry, author=request.user)
            success = True
            form = Feed_commentForm()
        
    else:
    
        form = Feed_commentForm()
    
    return render(request, 'feed_comment.html', {'entry' : entry, 'comments' : comments, 'form' : form, 'success' : success})
    
@login_required(login_url='/login/')
def profile(request):
 
    return render(request, 'profile.html')

@login_required(login_url='/login/')    
def messages(request):
    
    try:

        messages = private_message.objects.all().filter(recipient=request.user).order_by('-send_date')     
        active_message =  messages[0]

        page = request.GET.get('page', 1)
        paginator = Paginator(messages, 5)
		
        try:
            messages = paginator.page(page)
        except PageNotAnInteger:
            messages = paginator.page(1)
        except EmptyPage:
            messages = paginator.page(paginator.num_pages)
		
        return render(request, 'messages.html', {'messages' : messages, 'active_message' : active_message})

    except:
	
        return render(request, 'messages.html')
		
@login_required(login_url='/login/')
def view_message(request, id):
    
    try:
       
        messages = private_message.objects.all().filter(recipient=request.user).order_by('-send_date')     
        active_message =  private_message.objects.get(id=id)
        private_message.objects.filter(id=id).update(unread=False)

        page = request.GET.get('page', 1)
        paginator = Paginator(messages, 5)
		
        try:
            messages = paginator.page(page)
        except PageNotAnInteger:
            messages = paginator.page(1)
        except EmptyPage:
            messages = paginator.page(paginator.num_pages)
		
        return render(request, 'messages.html', {'messages' : messages, 'active_message' : active_message})

    except:
	
        return render(request, 'messages.html')

@login_required(login_url='/login/')	
def new_message(request):
    
    form = send_messageForm(request.POST)
 
    return render(request, 'new_message.html', {'form' : form})

@login_required(login_url='/login/')	
def send_message(request):
    
    form = send_messageForm(request.POST)
	
    if request.method == 'POST':
    
        form = send_messageForm(request.POST)
        
        if form.is_valid():
            
            cd = form.cleaned_data
            private_message.objects.create(body=cd['body'], sender=request.user, recipient=cd['recipient'])
            
            form = send_messageForm()
        
    else:
    
        form = send_messageForm()
        
    return HttpResponseRedirect('/messages')
    
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
