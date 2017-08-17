from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30)
    real_name = models.CharField(max_length=50)
    email = models.EmailField()
    created_on = models.DateField(default = timezone.now)
	
    class Meta:
       ordering = ['-created_on']