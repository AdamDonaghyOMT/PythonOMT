from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
	title = models.CharField(max_length=100)
	ownerUser = models.ForeignKey(User, unique=False)
	triggerPrice = models.FloatField()
	asx_code = models.CharField(max_length=3) #all asx codes are max length 3
	frequency = models.FloatField()