from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.db import models
from django.utils import timezone

# Create your models here.
	   
class User_profile(models.Model):
    
    owner = models.OneToOneField(User)
    info = models.TextField(max_length=210, blank = True)
	
    class Meta:
       ordering = ['owner']
	   
	   