from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from users import models as users
from django.template.defaultfilters import truncatewords

# Create your models here.

class Feed_entry(models.Model):
    

    body = models.TextField()
    author = models.ForeignKey(users.User, default=1)
    publish_date = models.DateTimeField(default = timezone.now)
	
    @property
    def content(self):
        return truncatewords(self.body, 10)
	
    def __str__(self):
   
	    return u'%s' % (self.author)
	
    class Meta:
       ordering = ['-publish_date']
       verbose_name = "Feed Entry"
       verbose_name_plural = "Feed Entries"