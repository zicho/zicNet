from __future__ import unicode_literals

from django.utils import timezone
from django.contrib.auth.models import User

from django.db import models
from django.utils import timezone

# Create your models here.
       
class User_profile(models.Model):
    
    owner = models.OneToOneField(User)
    info = models.TextField(max_length=210, blank = True)
    
    class Meta:
       ordering = ['owner']
      
class private_message(models.Model):
    
    sender = models.ForeignKey(User, related_name="sender")
    recipient = models.ForeignKey(User, related_name="recipient")
    body = models.TextField(max_length=420)
    send_date = models.DateTimeField(default = timezone.now)
    unread = models.BooleanField(default=True)