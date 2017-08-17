from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from users import models as users

# Create your models here.

class Feed_entry(models.Model):
    body = models.CharField(max_length=140)
    author = models.ForeignKey(users.User)
    publish_date = models.DateField(default = timezone.now)
	
    class Meta:
       ordering = ['-publish_date']