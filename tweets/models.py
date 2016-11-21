from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.db.models import Sum

#add the datefield to the models you're creating, also add UIDs
#that are unique to this model
from time import strftime, localtime

# Create your models here.

class Tweet(models.Model):
	uid=models.IntegerField(unique=True)
	source=models.TextField(max_length=None)
	date=models.DateField(null=False, default=strftime("%Y-%m-%d", localtime()))
        killed=models.IntegerField()
	state=models.CharField(max_length=20, default=None)


