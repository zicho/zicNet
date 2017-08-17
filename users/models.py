from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30)
    real_name = models.CharField(max_length=50, blank = True)
    email = models.EmailField(blank = True, verbose_name = "E-Mail")
    moderator = models.BooleanField(default=False)
	
    created_on = models.DateField(default = timezone.now)
	
    def __str__(self):
    
        if self.moderator == True:
            return u'%s (ID: %s) MODERATOR' % (self.username, self.id)
        else:
		    return u'%s (ID: %s)' % (self.username, self.id)
	
    class Meta:
       ordering = ['created_on']
	   
	   