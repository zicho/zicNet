"""zicNet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from zicNet.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^login/$', login_user),
    url(r'^logout/$', logout_user),
	
	url(r'^account_request/$', account_request),
	
    url(r'^password_change/$', password_change, name='password_change'),
    
	url(r'^feed/$', feed),
    url(r'^feed/(?P<id>[0-9]+)/$', comment_feed, name='comment_feed'),
	
    url(r'^feed/comment/(?P<id>[0-9]+)/$', quick_comment_feed, name='quick_comment_feed'),
	
    url(r'^profile/', profile),
	
	url(r'^messages/$', messages, name='messages'),
	url(r'^messages/new/$', new_message),
	url(r'^messages/send/$', send_message),
	
    url(r'^messages/(?P<id>[0-9]+)/$', view_message),
	
    #url(r'^search/', search),
]
