from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
    
class User(models.Model):
    
    username = models.CharField(max_length=30)
    real_name = models.CharField(max_length=50, blank = True)
    email = models.EmailField(blank = True, verbose_name = "E-Mail")
    moderator = models.BooleanField(default=False)
	
    created_on = models.DateTimeField(default = timezone.now)
	
    def __str__(self):
    
        if self.moderator == True:
            return u'%s (MOD)' % (self.username)
        else:
		    return u'%s' % (self.username)
	
    class Meta:
       ordering = ['created_on']
	   
class User_profile(models.Model):
    
    owner = models.ForeignKey(User, default=1)
    info = models.TextField(max_length=210, blank = True)
    
	
    created_on = models.DateTimeField(default = timezone.now)
	
    class Meta:
       ordering = ['owner']
	   
	   