from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import truncatewords

# Create your models here.

class Feed_entry(models.Model):

    body = models.TextField(max_length=20)
    author = models.ForeignKey(User)
    publish_date = models.DateTimeField(default = timezone.now)
	
    @property
    def content(self):
        return truncatewords(self.body, 10)
	
    def __str__(self):
   
	    return truncatewords(self.body, 1)
	
    class Meta:
       ordering = ['-publish_date']
       verbose_name = "Feed Entry"
       verbose_name_plural = "Feed Entries"

class Comment(models.Model):
    belongs_to = models.ForeignKey(Feed_entry, related_name='comments')
    author = models.ForeignKey(User, related_name='author')
    body = models.TextField(max_length=140)
    publish_date = models.DateTimeField(default = timezone.now)
    
    @property
    def content(self):
        return truncatewords(self.body, 10)
		
    def __unicode__(self):
	
        return self.body
	
    class Meta:
       ordering = ['-publish_date']